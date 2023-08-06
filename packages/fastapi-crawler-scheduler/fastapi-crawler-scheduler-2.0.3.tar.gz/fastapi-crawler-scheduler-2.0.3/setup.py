# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_crawler_scheduler',
 'fastapi_crawler_scheduler.service',
 'fastapi_crawler_scheduler.utils']

package_data = \
{'': ['*']}

install_requires = \
['APScheduler>=3.9.1,<4.0.0',
 'fastapi-utils>=0.2.1,<0.3.0',
 'fastapi>=0.85.0,<0.86.0',
 'redis>=4.3.4,<5.0.0',
 'uhashring>=2.1,<3.0']

setup_kwargs = {
    'name': 'fastapi-crawler-scheduler',
    'version': '2.0.3',
    'description': '',
    'long_description': '*********\n\n# fastapi_crawler_scheduler\n\n*********\n\n## 使用\n\n*********\n\n```python\nfrom fastapi_crawler_scheduler import TaskScheduler\nfrom fastapi import FastAPI\nimport uuid\n\napp = FastAPI()\ntask_scheduler = TaskScheduler(\n    app=app,\n    ssl=True,\n    project_name="project_name",\n    uuid_number=uuid.uuid4().__str__(),\n    redis_username=\'redis_username\',\n    redis_password=\'redis_password\',\n    redis_host="redis_host",\n    redis_port=6379,\n)\n\n\ndef add_spider(**crawler_info):\n    pass\n    print(f"add_spider = {crawler_info}")\n    print("add_spider")\n\n\ncrawler_info = {\n    "topic": "website_washingtonpost",\n    "name": "华盛顿邮报",\n    "base_url": "https://www.washingtonpost.com/arcio/news-sitemap/",\n    "news_node_tag": "url",\n    "title_tag": "news:title",\n    "url_tag": "loc",\n    "need_translation": 1,\n    "special_language_code": None,\n    "language_tag": "news:language",\n    "title_handler_name": "remove_cdata"\n}\n\n# 新增任务\ntask_scheduler.insert_task(func=add_spider, interval=4, job_id="job_1", crawler_info=crawler_info)\n# 更新任务\ntask_scheduler.update_task(func=add_spider, interval=4, job_id="job_1", crawler_info=crawler_info)\n# 删除任务\ntask_scheduler.delete_task(job_id="job_1")\n```\n\n### 参数介绍\n\n#### insert_task\n\n```python\n# func：Callable 定时任务函数\n# interval: int 任务间隔 \n# job_id: str 任务id\n# crawler_info: Dict = None 任务参数\n# trigger: str = "interval" 任务类型\n```\n\n#### update_task\n\n```python\n# func：Callable 定时任务函数\n# interval: int 任务间隔 \n# job_id: str 任务id\n# crawler_info: Dict = None 任务参数\n# trigger: str = "interval" 任务类型\n```\n\n#### delete_task\n\n```python\n# job_id: str 任务id\n```\n\n安装\n============\nPypi\n----\n\n    $ pip install fastapi-crawler-scheduler\n\n',
    'author': 'laowang',
    'author_email': '847063657@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
