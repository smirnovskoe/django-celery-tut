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
