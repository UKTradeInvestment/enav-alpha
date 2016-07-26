from django.views.generic import FormView, TemplateView
from apps.markets.views.generics import EnavTemplateView, EnavFormView
from .forms import ProductChoiceForm, RegionChoiceForm


class HomepageView(EnavTemplateView):
    template_name = 'homepage.html'


class RegionChoiceView(EnavFormView):
    form_class = RegionChoiceForm
    template_name = 'region-choice.html'


class ProductChoiceView(EnavFormView):
    form_class = ProductChoiceForm
    template_name = 'product-choice.html'

    def get_context_data(self, **kwargs):
        context = super(ProductChoiceView, self).get_context_data(**kwargs)
        context['regions'] = self.request.GET.getlist('region')
        return context
