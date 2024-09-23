
from celery import shared_task


@shared_task
def task1():
    print('This is an example task')
    return