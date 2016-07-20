from django.views.generic import FormView, TemplateView

from .forms import ProductChoiceForm, RegionChoiceForm


class HomepageView(TemplateView):
    template_name = 'homepage.html'


class RegionChoiceView(FormView):
    form_class = RegionChoiceForm
    template_name = 'region-choice.html'


class ProductChoiceView(FormView):
    form_class = ProductChoiceForm
    template_name = 'product-choice.html'

    def get_context_data(self, **kwargs):
        context = super(ProductChoiceView, self).get_context_data(**kwargs)
        context['regions'] = self.request.GET.getlist('region')
        return context
