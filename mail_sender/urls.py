from django.urls import path

from . import views

app_name = 'mail_sender'

urlpatterns = [
    path('', views.ContactView.as_view(), name='contact'),
]
