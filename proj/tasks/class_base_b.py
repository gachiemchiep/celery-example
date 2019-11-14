from __future__ import absolute_import
from celery import Task
from proj.celery import app


class CustomTask(Task):
    def run(self):
        print('running')
CustomTask = app.register_task(CustomTask())