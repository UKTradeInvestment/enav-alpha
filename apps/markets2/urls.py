from django.conf.urls import url
from . import views

app_name = 'markets2'

urlpatterns = [
    url(r'^markets/$', views.MarketListView.as_view(), name='list'),
]
