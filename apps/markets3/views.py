import json

from django.http import JsonResponse
from django.views.generic import ListView, DetailView, FormView
from .models import Market
from .forms import MarketFilterForm


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


class MarketCountView(MarketListView):
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(
            {'count': self.object_list.count()},
            **response_kwargs
        )


class MarketDetailView(DetailView):
    model = Market
    template_name = 'markets3/detail.html'


class FilteringView(FormView):
    form_class = MarketFilterForm
    template_name = 'markets3/filtering.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['results_count'] = Market.objects.count()
        return context
