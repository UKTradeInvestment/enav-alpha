from django.conf.urls import url
from django.contrib import admin
from apps.homepage.views import Homepage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^$',
        Homepage.as_view(),
        name='homepage'
    ),
]
