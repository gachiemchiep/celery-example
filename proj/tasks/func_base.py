from __future__ import absolute_import
from proj.celery import app


@app.task
def split():
    task_count = 10
    return task_count

@app.task
def run(task_count):
    for i in range(task_count):
        subtask.delay(i)

@app.task
def subtask(index):
    print("Processing " + str(index))