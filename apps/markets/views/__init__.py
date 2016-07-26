from django.shortcuts import render

from .generics import EnavListView, EnavDetailView
from ..models import Market, Logo
from ..forms import MarketFilterForm


class MarketListView(EnavListView):
    template_name = 'list.html'
    context_object_name = 'markets_list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = MarketFilterForm(self.request.GET)
        return context

    def get_queryset(self):
        _filter = {}

        for key, items in self.request.GET.lists():
            _filter["{}__in".format(key)] = items

        return Market.objects.filter(**_filter).distinct()


class MarketDetailView(EnavDetailView):
    model = Market
    template_name = 'detail.html'
