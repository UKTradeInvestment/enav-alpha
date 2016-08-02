from django.conf.urls import url
from . import views

app_name = 'markets1'

urlpatterns = [
    url(r'^$', views.ArticleView.as_view(), name='articles'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticletDetailView.as_view(), name='article'),
    url(r'^markets/$', views.MarketsView.as_view(), name='markets'),
]
