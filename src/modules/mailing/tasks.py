from celery import shared_task


@shared_task
def add():
    print('Hi!')