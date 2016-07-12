from django.views import generic
from django.shortcuts import render

from .models import Market


class MarketListView(generic.ListView):
    template_name = 'markets/list.html'
    context_object_name = 'markets_list'

    def get_queryset(self):
        return Market.objects.all()


class MarketDetailView(generic.DetailView):
    model = Market
    template_name = 'markets/detail.html'
