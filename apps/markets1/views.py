from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Market, Article


class MarketsView(ListView):
    template_name = 'markets1/list.html'
    context_object_name = 'markets_list'
    model = Market

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles_list'] = Article.objects.all()
        return context


class ArticletDetailView(DetailView):
    template_name = 'markets1/list.html'
    context_object_name = 'article'
    model = Article

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['articles_list'] = Article.objects.all()
        return context


class ArticleView(ListView):
    template_name = 'markets1/list.html'
    context_object_name = 'articles_list'
    model = Article
