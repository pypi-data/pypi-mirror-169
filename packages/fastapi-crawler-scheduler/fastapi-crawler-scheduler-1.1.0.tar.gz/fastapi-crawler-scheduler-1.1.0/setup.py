# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_crawler_scheduler',
 'fastapi_crawler_scheduler.apscheduler',
 'fastapi_crawler_scheduler.apscheduler.executors',
 'fastapi_crawler_scheduler.apscheduler.jobstores',
 'fastapi_crawler_scheduler.apscheduler.schedulers',
 'fastapi_crawler_scheduler.apscheduler.triggers',
 'fastapi_crawler_scheduler.apscheduler.triggers.cron',
 'fastapi_crawler_scheduler.service',
 'fastapi_crawler_scheduler.service_old',
 'fastapi_crawler_scheduler.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyQt5>=5.15.7,<6.0.0',
 'SQLAlchemy>=1.4.41,<2.0.0',
 'fastapi-utils>=0.2.1,<0.3.0',
 'fastapi>=0.85.0,<0.86.0',
 'funcsigs>=1.0.2,<2.0.0',
 'kazoo>=2.8.0,<3.0.0',
 'pytz>=2022.2.1,<2023.0.0',
 'redis>=4.3.4,<5.0.0',
 'rethinkdb>=2.4.9,<3.0.0',
 'setuptools>=65.4.0,<66.0.0',
 'six>=1.16.0,<2.0.0',
 'tornado>=6.2,<7.0',
 'tzlocal>=4.2,<5.0']

setup_kwargs = {
    'name': 'fastapi-crawler-scheduler',
    'version': '1.1.0',
    'description': '',
    'long_description': '',
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
