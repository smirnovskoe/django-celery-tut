from django.views.generic import CreateView


class ContactView(CreateView):
    template_name = 'mail_sender/contact.html'
    form_class = None
    success_url = '/'
