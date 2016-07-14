from django.conf.urls import url
from . import views

app_name = 'markets'

urlpatterns = [
    url(r'^$', views.HomepageView.as_view(), name='home'),
    url(r'^compare$', views.MarketListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.MarketDetailView.as_view(), name='detail'),
]
