from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Market, Article


class MainView(TemplateView):
    template_name = 'markets1/list.html'

    def _get_links(self):
        articles = Article.objects.all()
        links = [(article.title, reverse('markets1:item', args=['article', article.pk])) for article in articles]
        links.append(('E-marketplaces overseas', reverse('markets1:item', args=['markets'])))
        links.sort(key=lambda x: x[0])
        return links

    def get_context_data(self, mode=None, pk=None, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['links'] = self._get_links()
        if mode == 'markets':
            context['markets_list'] = Market.objects.all()
        if mode == 'article' and pk is not None:
            context['article'] = Article.objects.get(pk=pk)

        return context
