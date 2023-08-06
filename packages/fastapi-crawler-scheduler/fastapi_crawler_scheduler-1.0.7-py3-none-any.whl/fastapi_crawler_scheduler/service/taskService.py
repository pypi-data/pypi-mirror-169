from typing import Callable, Dict
import os

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from apscheduler.util import obj_to_ref

from fastapi_crawler_scheduler.utils.exception import SchedulerError
from fastapi_crawler_scheduler.service.dbRedisHelper import DbRedisHelper
from fastapi_crawler_scheduler.service.baseScheduler import BaseScheduler


class TaskScheduler(object):

    def __init__(self,
                 app: FastAPI,
                 project_name: str,
                 uuid_number: str,
                 ssl: bool,
                 thread_pool_size: int = 10,
                 job_coalesce: bool = True,
                 job_max_instance: int = 1,
                 job_misfire_grace_time: int = 10,
                 redis_host: str = "127.0.0.1",
                 redis_port: int = 6379,
                 username: str = None,
                 password: str = None,
                 ):
        self.app = app
        self.ssl = ssl
        self.project_name = project_name
        self.uuid_number = uuid_number
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.username = username
        self.password = password
        self.jobs_key = self.project_name + ':apscheduler:jobs:' + str(os.getpid())
        self.run_times_key = self.project_name + ':apscheduler:run_times:' + str(os.getpid())
        self.thread_pool_size = thread_pool_size
        self.job_coalesce = job_coalesce
        self.job_max_instance = job_max_instance
        self.job_misfire_grace_time = job_misfire_grace_time
        # 实现 scheduler 注册
        self.register_scheduler()
        self.register_redis_db = DbRedisHelper(
            project_name=self.project_name,
            redis_host=self.redis_host,
            redis_port=self.redis_port,
            username=self.username,
            password=self.password,
            ssl=self.ssl,
        )
        self.register_base_scheduler = BaseScheduler(
            project_name=self.project_name,
            redis_db=self.register_redis_db,
            scheduler=self.scheduler,
            uuid_number=self.uuid_number,
            redis_job_store=self.redis_job_store
        )
        self.register_async_task()

    def register_async_task(self):
        @repeat_every(seconds=5)
        def check_process():
            self.register_base_scheduler.check_process()

        @repeat_every(seconds=8)
        def check_scheduler_run():
            self.register_base_scheduler.run()

        @repeat_every(seconds=10)
        def check_redis_jobstores():
            self.register_base_scheduler.check_redis_jobstores()

        def scheduler_start():
            self.scheduler.start()

        self.app.on_event("startup")(check_process)
        self.app.on_event("startup")(check_scheduler_run)
        self.app.on_event("startup")(check_redis_jobstores)
        self.app.on_event("startup")(scheduler_start)

    def register_scheduler(self):
        redis_job_store = getattr(self.app, "redis_job_store", None)
        if redis_job_store is None:
            redis_job_store = RedisJobStore(
                host=self.redis_host,
                port=self.redis_port,
                username=self.username,
                password=self.password,
                jobs_key=self.jobs_key,
                run_times_key=self.run_times_key,
                ssl=self.ssl,
            )
        self.redis_job_store = redis_job_store
        setattr(self.app, "redis_job_store", self.redis_job_store)
        scheduler = getattr(self.app, "scheduler", None)
        if scheduler is None:
            scheduler = BackgroundScheduler()
            scheduler.configure(
                jobstores={
                    "default": self.redis_job_store
                },
                executors={
                    "default": ThreadPoolExecutor(
                        max_workers=self.thread_pool_size,
                    )
                },
                job_defaults={
                    "coalesce": self.job_coalesce,
                    "max_instance": self.job_max_instance,
                    "misfire_grace_time": self.job_misfire_grace_time,
                }
            )
        elif isinstance(scheduler, BackgroundScheduler):
            pass
        else:
            raise SchedulerError("FastAPI应用已经包含scheduler对象，但是该对象并非BackgroundScheduler")
        self.scheduler = scheduler
        setattr(self.app, "scheduler", self.scheduler)

    def insert_task(
            self,
            func: Callable,
            interval: int,
            job_id: str,
            crawler_info: Dict = None,
            trigger: str = "interval",
    ):
        redis_dict = dict()
        redis_dict['func'] = obj_to_ref(func)
        redis_dict['interval'] = interval
        redis_dict['job_id'] = job_id
        redis_dict['trigger'] = trigger
        if crawler_info is not None:
            redis_dict.update(crawler_info)
        self.register_base_scheduler.insert_task(redis_dict)

    def update_task(
            self,
            func: Callable,
            interval: int,
            job_id: str,
            crawler_info: Dict = None,
            trigger: str = "interval",
    ):
        redis_dict = dict()
        redis_dict['func'] = obj_to_ref(func)
        redis_dict['interval'] = interval
        redis_dict['job_id'] = job_id
        redis_dict['trigger'] = trigger
        if crawler_info is not None:
            redis_dict.update(crawler_info)
        self.register_base_scheduler.update_task(redis_dict)

    def delete_task(
            self,
            job_id: str,
    ):
        self.register_base_scheduler.delete_task(job_id=job_id)
