from core.celery import app

from .service import test_task


@app.task
def send_email_by_celery(user):
    test_task(10, 10)
