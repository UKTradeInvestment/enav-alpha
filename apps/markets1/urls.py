from django.conf.urls import url
from . import views

app_name = 'markets1'

urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='home'),
    url(r'^(?P<mode>[a-z]+)/$', views.MainView.as_view(), name='item'),
    url(r'^(?P<mode>[a-z]+)/(?P<pk>[0-9]+)/$', views.MainView.as_view(), name='item'),
]
