from unittest import mock
from django.test import TestCase

from .forms import ContactForm
from .views import ContactView, ContactThanksView


initial_data = {
    'contact_name': 'Spam Eggs',
    'contact_email': 'spam@example.com',
    'content': 'testing contact form'
}


class ContactFormTests(TestCase):

    def test_form_valid(self):
        form = ContactForm()
        self.assertFalse(form.is_valid())
        form = ContactForm(initial_data, initial=initial_data)
        self.assertTrue(form.is_valid())

    @mock.patch('django.core.mail.EmailMessage.send')
    def test_send_email(self, send_mail_mock):
        form = ContactForm(initial_data, initial=initial_data)
        form.is_valid()
        form.send_email()
        self.assertTrue(send_mail_mock.called)
