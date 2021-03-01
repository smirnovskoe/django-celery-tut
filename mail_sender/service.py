from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Тестовая рассылка писем',
        'Пожалуйста не отвечайте на данное письмо',
        'asdas',
        [user_email, ],
        fail_silently=False,
    )


def test_task(a: int, b: int):
    for _ in range(100):
        a += b
