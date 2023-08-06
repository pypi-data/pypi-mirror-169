*********

# fastapi_crawler_scheduler

*********

## 使用

*********

```python
from fastapi_crawler_scheduler import TaskScheduler
from fastapi import FastAPI
import uuid

app = FastAPI()
task_scheduler = TaskScheduler(
    app=app,
    ssl=True,
    project_name="project_name",
    uuid_number=uuid.uuid4().__str__(),
    redis_username='redis_username',
    redis_password='redis_password',
    redis_host="redis_host",
    redis_port=6379,
)


def add_spider(**crawler_info):
    pass
    print(f"add_spider = {crawler_info}")
    print("add_spider")


crawler_info = {
    "topic": "website_washingtonpost",
    "name": "华盛顿邮报",
    "base_url": "https://www.washingtonpost.com/arcio/news-sitemap/",
    "news_node_tag": "url",
    "title_tag": "news:title",
    "url_tag": "loc",
    "need_translation": 1,
    "special_language_code": None,
    "language_tag": "news:language",
    "title_handler_name": "remove_cdata"
}

# 新增任务
task_scheduler.insert_task(func=add_spider, interval=4, job_id="job_1", crawler_info=crawler_info)
# 更新任务
task_scheduler.update_task(func=add_spider, interval=4, job_id="job_1", crawler_info=crawler_info)
# 删除任务
task_scheduler.delete_task(job_id="job_1")
```

### 参数介绍

#### insert_task

```python
# func：Callable 定时任务函数
# interval: int 任务间隔 
# job_id: str 任务id
# crawler_info: Dict = None 任务参数
# trigger: str = "interval" 任务类型
```

#### update_task

```python
# func：Callable 定时任务函数
# interval: int 任务间隔 
# job_id: str 任务id
# crawler_info: Dict = None 任务参数
# trigger: str = "interval" 任务类型
```

#### delete_task

```python
# job_id: str 任务id
```

安装
============
Pypi
----

    $ pip install fastapi-crawler-scheduler

