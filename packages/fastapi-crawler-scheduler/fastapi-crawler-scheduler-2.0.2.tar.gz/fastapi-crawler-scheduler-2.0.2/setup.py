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
    'version': '2.0.2',
    'description': '',
    'long_description': '*********\nfastapi_crawler_scheduler\n*********\n\nUsage\n=====\n\n.. code-block:: python\n\n    from fastapi_crawler_scheduler import TaskScheduler\n    from fastapi import FastAPI\n    import uuid\n\n    app = FastAPI()\n    task_scheduler = TaskScheduler(\n\n        app=app,\n        ssl=True,\n        project_name="project_name",\n        uuid_number=uuid.uuid4().__str__(),\n        redis_username=\'redis_username\',\n        redis_password=\'redis_password\',\n        redis_host="redis_host",\n        redis_port=6379,\n    )\n\n\nInstallation\n============\nPypi\n----\nUsing pip:\n\n.. code-block:: sh\n\n    $ pip install fastapi-crawler-scheduler\n\n',
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
