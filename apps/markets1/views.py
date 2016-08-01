from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView


class MarketsView(TemplateView):
    template_name = 'main.html'
