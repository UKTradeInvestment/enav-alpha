from django.conf.urls import url
from . import views

app_name = 'markets3'

urlpatterns = [
    url(r'^$', views.FilteringView.as_view(), name='filtering'),
    url(r'^markets/$', views.MarketListView.as_view(), name='list'),
    url(r'^markets/(?P<pk>[0-9]+)/$', views.MarketDetailView.as_view(), name='detail'),
]
