import os
import json
from typing import List
import six
from time import time

from uhashring import HashRing
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.util import ref_to_obj

from fastapi_crawler_scheduler.service.dbRedisHelper import DbRedisHelper, standard_time

setp = 1


def div_list(tem_lists: List[any]) -> list:
    back_lists = list()
    tem_num = len(tem_lists)
    end_num = int(tem_num / setp)
    for i in range(end_num):
        ss = tem_lists[i * setp:(i + 1) * setp]
        back_lists.append(ss)
    back_lists.append(tem_lists[end_num * setp:])
    return back_lists


def format_params(params) -> dict:
    for key in ['func', 'interval', 'job_id', 'trigger', 'operation', 'is_change', 'process_node_id', 'details', ]:
        try:
            del params[key]
        except KeyError:
            pass

    return params


class BaseScheduler(object):

    def __init__(
            self,
            redis_db: DbRedisHelper,
            scheduler: BackgroundScheduler,
            uuid_number: str,
            project_name: str,
            redis_job_store: RedisJobStore,

    ) -> None:
        self.uuid_number = uuid_number
        self.project_name = project_name
        self.redis_db = redis_db
        self.scheduler = scheduler
        self.process_id_list = []
        self.redis_job_store = redis_job_store

    def scheduler_add_job(
            self,
            **crawler_info
    ) -> None:
        try:
            func = ref_to_obj(crawler_info.get('func'))
        except Exception as e:
            print(e)
            print("函数有问题")
            return
        interval = crawler_info.get('interval')
        trigger = crawler_info.get('trigger')
        job_id = crawler_info.get('job_id')
        if self.redis_job_store.redis.hexists(self.redis_job_store.jobs_key, job_id):
            self.redis_job_store.remove_job(job_id=job_id)
        crawler_info = format_params(params=crawler_info)
        self.scheduler.add_job(
            func,
            id=job_id,
            trigger=trigger,
            kwargs=crawler_info,
            seconds=interval,
        )

    def check_process(self) -> None:
        self.redis_db.process_acquire(f'{self.project_name}:node:{self.uuid_number}:{os.getpid()}')

    def get_process_list(self) -> list:
        return self.redis_db.get_proces_info()

    def process_check_count(self, process_id: int, check_key: str) -> None:
        if process_id not in self.process_id_list:
            if self.redis_db.acquire(lock_name=check_key):
                check_value = self.redis_db.from_key_get_value(key_name=check_key)
                if check_value is None:
                    return None
                check_process_number = check_value.get('check_process_number')
                if check_process_number is None:
                    check_process_number = 1
                else:
                    check_process_number += 1
                if check_process_number >= 2:
                    self.redis_db.delete_key(lock_name=check_key)
                else:
                    check_value['check_process_number'] = check_process_number
                    self.redis_db.string_set(key=check_key, value=json.dumps(check_value, ensure_ascii=False))
                self.redis_db.release(lock_name=check_key)

    def check_backend_task(self) -> None:
        node_process_id_list = self.get_process_list()
        self.process_id_list = [int(str(node_id).strip().split(':')[-1]) for node_id in node_process_id_list]
        # 处理后端操作
        hr = HashRing(nodes=node_process_id_list)
        backend_task = self.redis_db.get_backend_task()
        backend_key_list = div_list(tem_lists=backend_task)
        for key_list in backend_key_list:
            for backend_key, backend_info in self.redis_db.get_tasks(keys=key_list).items():
                if backend_info is None:
                    continue
                lock_all_backend_key = f'{self.redis_db.prefix}:all:{backend_info["job_id"]}'
                all_backend_key = f'{self.project_name}:all:{backend_info["job_id"]}'
                if not self.redis_db.lock_exists(lock_name=lock_all_backend_key):
                    process_node_id = hr.get_node(backend_info["job_id"])
                    backend_info['process_node_id'] = process_node_id
                    self.redis_db.string_set(key=all_backend_key, value=json.dumps(backend_info, ensure_ascii=False))
                    self.redis_db.delete_key(lock_name=backend_key)

    def check_all_task(self) -> None:
        node_process_id_list = self.get_process_list()
        self.process_id_list = [int(str(node_id).strip().split(':')[-1]) for node_id in node_process_id_list]
        hr = HashRing(nodes=node_process_id_list)
        # 处理 all_task
        all_task = self.redis_db.get_all_task()
        all_task_key_list = div_list(tem_lists=all_task)
        for key_list in all_task_key_list:
            for all_key, all_value in self.redis_db.get_tasks(keys=key_list).items():
                if self.redis_db.acquire(lock_name=all_key):
                    if all_value is None:
                        continue
                    redis_process_node_id = all_value["process_node_id"]
                    new_process_node_id = hr.get_node(all_value["job_id"])
                    if new_process_node_id == redis_process_node_id:
                        process_id = int(str(redis_process_node_id).strip().split(':')[-1])
                        # 进程没变化
                        if all_value['is_change'] == 1:
                            next_key = f'{self.project_name}:{all_value["operation"]}:{self.uuid_number}:{all_value["job_id"]}:{process_id}'
                            self.redis_db.string_set(key=next_key, value=json.dumps(all_value, ensure_ascii=False))
                            all_value["is_change"] = 0
                            self.redis_db.string_set(key=all_key, value=json.dumps(all_value, ensure_ascii=False))
                        else:
                            pass
                    else:
                        # 进程有变化
                        new_process_id = int(str(new_process_node_id).strip().split(':')[-1])
                        redis_process_id = int(str(redis_process_node_id).strip().split(':')[-1])
                        delete_key = f'{self.project_name}:delete:{self.uuid_number}:{all_value["job_id"]}:{redis_process_id}'
                        all_value["details"] = "删除任务"
                        self.redis_db.string_set(key=delete_key, value=json.dumps(all_value, ensure_ascii=False))
                        all_value["process_node_id"] = new_process_node_id
                        if all_value['operation'] == 'delete':
                            # 无需向下一步添加任务
                            pass
                        else:
                            insert_key = f'{self.project_name}:insert:{self.uuid_number}:{all_value["job_id"]}:{new_process_id}'
                            all_value["details"] = "进程变化，新增任务"
                            self.redis_db.string_set(key=insert_key, value=json.dumps(all_value, ensure_ascii=False))
                        all_value["is_change"] = 0
                        self.redis_db.string_set(key=all_key, value=json.dumps(all_value, ensure_ascii=False))
                    self.redis_db.release(lock_name=all_key)

    def check_insert_task(self) -> None:
        # 处理 insert_task
        insert_task = self.redis_db.get_insert_task()
        insert_task_key_list = div_list(tem_lists=insert_task)
        for key_list in insert_task_key_list:
            for insert_key, insert_value in self.redis_db.get_tasks(keys=key_list).items():
                try:
                    if insert_value is None:
                        continue
                    process_node_id = insert_value['process_node_id']
                    apscheduler_id = insert_value['job_id']
                    process_id = int(str(process_node_id).strip().split(':')[-1])
                    if os.getpid() == process_id:
                        if self.scheduler.get_job(job_id=apscheduler_id):
                            self.scheduler.remove_job(job_id=apscheduler_id)
                        self.scheduler_add_job(**insert_value)
                        self.redis_db.delete_key(lock_name=insert_key)
                    else:
                        self.process_check_count(process_id=process_id, check_key=insert_key)
                except Exception as e:
                    print(e)

    def check_update_task(self) -> None:
        # 处理 update_task
        update_task = self.redis_db.get_update_task()
        update_task_key_list = div_list(tem_lists=update_task)
        for key_list in update_task_key_list:
            for update_key, update_value in self.redis_db.get_tasks(keys=key_list).items():
                try:
                    if update_value is None:
                        continue
                    process_node_id = update_value['process_node_id']
                    apscheduler_id = update_value['job_id']
                    process_id = int(str(process_node_id).strip().split(':')[-1])
                    if os.getpid() == process_id:
                        if self.scheduler.get_job(job_id=apscheduler_id):
                            self.scheduler.remove_job(job_id=apscheduler_id)
                        self.scheduler_add_job(**update_value)
                        self.redis_db.delete_key(lock_name=update_key)
                    else:
                        self.process_check_count(process_id=process_id, check_key=update_key)
                except Exception as e:
                    print(e)

    def check_delete_task(self) -> None:

        # 处理 delete_task
        delete_task = self.redis_db.get_delete_task()
        delete_task_key_list = div_list(tem_lists=delete_task)
        for key_list in delete_task_key_list:
            for delete_key, delete_value in self.redis_db.get_tasks(keys=key_list).items():
                try:
                    if delete_value is None:
                        continue
                    process_node_id = delete_value['process_node_id']
                    apscheduler_id = delete_value['job_id']
                    process_id = int(str(process_node_id).strip().split(':')[-1])
                    if os.getpid() == process_id:
                        if self.scheduler.get_job(job_id=apscheduler_id):
                            self.scheduler.remove_job(job_id=apscheduler_id)
                        self.redis_db.delete_key(lock_name=delete_key)
                        self.redis_db.delete_key(
                            lock_name=f'{self.project_name}:running_job:{os.getpid()}:{apscheduler_id}')
                    else:
                        self.process_check_count(process_id=process_id, check_key=delete_key)
                except Exception as e:
                    print(e)

    def insert_task(self, crawler_info: dict) -> dict:
        crawler_info['operation'] = 'insert'
        crawler_info['is_change'] = 1
        self.redis_db.string_set(f'{self.project_name}:backend:{crawler_info.get("job_id")}',
                                 json.dumps(crawler_info, ensure_ascii=False))
        return {"is_ok": 1, "reason": f"insert success {crawler_info['job_id']}"}

    def update_task(self, crawler_info: dict) -> dict:
        crawler_info['operation'] = 'update'
        crawler_info['is_change'] = 1
        self.redis_db.string_set(f'{self.project_name}:backend:{crawler_info.get("job_id")}',
                                 json.dumps(crawler_info, ensure_ascii=False))
        return {"is_ok": 1, "reason": f"update success {crawler_info['job_id']}"}

    def delete_task(self, job_id: str) -> dict:
        crawler_info = dict()
        crawler_info['job_id'] = job_id
        crawler_info['is_change'] = 1
        crawler_info['operation'] = 'delete'
        self.redis_db.string_set(f'{self.project_name}:backend:{crawler_info.get("job_id")}',
                                 json.dumps(crawler_info, ensure_ascii=False))
        return {"is_ok": 1, "reason": f"delete success {crawler_info['job_id']}"}

    def sync_scheduler_job_to_redis(self) -> None:
        job_list = self.scheduler.get_jobs()
        for job in job_list:
            key = f'{self.project_name}:running_job:{os.getpid()}:{job.id}'
            lock_value = standard_time()
            self.redis_db.process_acquire(lock_name=key, lock_value=lock_value, expire_time=300)

    def check_redis_jobstores(self):
        job_process_dict = {}
        all_task = self.redis_db.get_all_task()
        all_task_key_list = div_list(tem_lists=all_task)
        for key_list in all_task_key_list:
            for all_key, all_value in self.redis_db.get_tasks(keys=key_list).items():
                if all_value is None:
                    continue
                process_node_id = all_value["process_node_id"]
                job_id = all_value["job_id"]
                process_id = int(str(process_node_id).strip().split(':')[-1])
                job_process_dict[job_id] = process_id
        if len(job_process_dict) == 0:
            return job_process_dict
        stores_job_task = self.redis_db.get_stores_job_task()
        for stores_job_key in stores_job_task:
            stores_job_run_times_key = stores_job_key.replace('jobs', 'run_times')
            job_states = self.redis_job_store.redis.hgetall(stores_job_key)
            for job_id, job_state in six.iteritems(job_states):
                job_id = job_id.decode('utf-8')
                try:
                    belongs_to_process_id = job_process_dict[job_id]
                except KeyError:
                    continue
                try:
                    stores_job_process_id = int(stores_job_key.split(':')[-1])
                except ValueError:
                    continue
                if stores_job_process_id == belongs_to_process_id:
                    pass
                else:
                    # 删除
                    if self.redis_job_store.redis.hexists(stores_job_key, job_id):
                        pass
                        with self.redis_job_store.redis.pipeline() as pipe:
                            pipe.hdel(stores_job_key, job_id)
                            pipe.zrem(stores_job_run_times_key, job_id)
                            pipe.execute()
                    continue
                # print("*************************************************************")
                # print(f"job {job}")
                # print(f"belongs_to_process_id {belongs_to_process_id}")
                # print("----------------------------------------------------------------")

    def run(self) -> None:
        # start_time = time()
        self.check_backend_task()
        self.check_all_task()
        self.check_insert_task()
        self.check_update_task()
        self.check_delete_task()
        self.sync_scheduler_job_to_redis()
        # print("*************************************")
        # end_time = time()
        # print(f"耗时： {end_time - start_time} seconds since")
