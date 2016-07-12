from django.conf.urls import url, include
from django.contrib import admin
from apps.homepage.views import Homepage

urlpatterns = [
    url(r'^markets/', include('apps.markets.urls'), name="markets"),
    url(r'^admin/', admin.site.urls),
    url(r'^$', Homepage.as_view(), name='homepage'),
]
