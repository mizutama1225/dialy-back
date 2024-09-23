from celery import shared_task


@shared_task
def random_send():
    print('This is an example task')
    return