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
 'fastapi>=0.85.0,<0.86.0']

setup_kwargs = {
    'name': 'fastapi-crawler-scheduler',
    'version': '1.0.2',
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
