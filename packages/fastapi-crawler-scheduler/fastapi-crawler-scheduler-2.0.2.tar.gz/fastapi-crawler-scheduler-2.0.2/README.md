*********
fastapi_crawler_scheduler
*********

Usage
=====

.. code-block:: python

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


Installation
============
Pypi
----
Using pip:

.. code-block:: sh

    $ pip install fastapi-crawler-scheduler

