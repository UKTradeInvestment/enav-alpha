from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy

from .forms import ContactForm


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['originating_page'] = self.request.GET.get('originating_page')
        return kwargs


class ContactThanksView(TemplateView):
    template_name = 'thanks.html'
