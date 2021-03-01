from core.celery import app
from .models import Contact
from .service import test_task


@app.task
def send_email_by_celery(user_email):
    # send(user_email)
    test_task(10, 10)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        # send(user_email)
        test_task(10, 10)


@app.task()
def my_task(a, b):
    c = a + b
    return c


@app.task(bind=True, default_retry_delay=1 * 60)
def my_task_retry(self, x, y):
    try:
        return x + y
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
