from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import Market
from .forms import MarketFilterForm, RegionChoiceForm, ProductChoiceForm


class MarketListView(ListView):
    template_name = 'markets3/list.html'
    context_object_name = 'markets_list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = MarketFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        _filter = {}

        for key, items in self.request.GET.lists():
            attr = key.split('__')[0]
            try:
                Market._meta.get_field(attr)
                _filter["{}__in".format(key)] = items
            except:
                # Ignore GET params that aren't on the model
                pass

        return Market.objects.filter(**_filter).distinct()


class MarketDetailView(DetailView):
    model = Market
    template_name = 'markets3/detail.html'


class RegionChoiceView(FormView):
    form_class = RegionChoiceForm
    template_name = 'markets3/region-choice.html'


class ProductChoiceView(FormView):
    form_class = ProductChoiceForm
    template_name = 'markets3/product-choice.html'

    def get_context_data(self, **kwargs):
        context = super(ProductChoiceView, self).get_context_data(**kwargs)
        context['regions'] = self.request.GET.getlist('region')
        return context
