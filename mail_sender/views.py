from django.views.generic import CreateView

from .forms import ContactModelForm
from .models import Contact
from .service import send, test_task
from .tasks import send_email_by_celery


class ContactView(CreateView):
    model = Contact
    form_class = ContactModelForm
    success_url = '/'
    template_name = 'mail_sender/contact.html'

    def form_valid(self, form: ContactModelForm):
        form.save()
        # send(form.instance.email)
        send_email_by_celery.delay(form.instance.email)
        return super().form_valid(form)
