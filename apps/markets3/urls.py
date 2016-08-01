from django.conf.urls import url
from . import views

app_name = 'markets3'

urlpatterns = [
    url(r'^$', views.RegionChoiceView.as_view(), name='region-choice'),
    url(r'^category/$', views.ProductChoiceView.as_view(), name='product-choice'),
    url(r'^markets/$', views.MarketListView.as_view(), name='list'),
    url(r'^markets/(?P<pk>[0-9]+)/$', views.MarketDetailView.as_view(), name='detail'),
]
