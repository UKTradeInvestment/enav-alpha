from django.conf.urls import url
from . import views

app_name = 'contact'

urlpatterns = [
    url(r'^$', views.ContactView.as_view(), name='submit'),
    url(r'^thanks/$', views.ContactThanksView.as_view(), name='thanks'),
]
