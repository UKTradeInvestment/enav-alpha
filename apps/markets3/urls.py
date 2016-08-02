from django.conf.urls import url
from . import views

app_name = 'markets3'

urlpatterns = [
    url(r'^$', views.HomepageView.as_view(), name='home3'),
    url(r'^filter/$', views.FilteringView.as_view(), name='filtering'),
    url(r'^markets/$', views.MarketListView.as_view(), name='list'),
    url(r'^markets/count\.json$', views.MarketCountView.as_view(), name='count'),
    url(r'^markets/(?P<pk>[0-9]+)/$', views.MarketDetailView.as_view(), name='detail'),
]
