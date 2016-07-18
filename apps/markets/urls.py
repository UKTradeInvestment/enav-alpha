from django.conf.urls import url
from . import views

app_name = 'markets'

urlpatterns = [
    url(r'^$', views.MarketListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.MarketDetailView.as_view(), name='detail'),
]
