from django.conf.urls import url
from . import views

app_name = 'markets1'

urlpatterns = [
    url(r'^$', views.MarketsView.as_view(), name='list'),
]