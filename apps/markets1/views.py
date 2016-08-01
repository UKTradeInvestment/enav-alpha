from django.shortcuts import render
from django.views.generic import ListView
from .models import Market


class MarketsView(ListView):
    template_name = 'markets1/list.html'
    context_object_name = 'markets_list'
    model = Market
