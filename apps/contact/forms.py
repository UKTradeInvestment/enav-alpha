from django import forms
from django.core.mail import EmailMessage
from django.conf import settings


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    originating_page = forms.CharField(required=False, widget=forms.HiddenInput())
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def send_email(self):
        data = self.cleaned_data
        recipients = [admin[1] for admin in settings.ADMINS]
        body = "{0}\n\nUser was at: {1}".format(data['content'], data['originating_page'])

        email = EmailMessage(
            "New contact form submission",
            body,
            data['contact_name'],
            recipients,
            headers={'Reply-To': data['contact_email']}
        )
        email.send()
