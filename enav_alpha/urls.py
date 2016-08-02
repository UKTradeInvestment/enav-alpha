from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.core.views import HomepageView


urlpatterns = [
    url(r'^1/', include('apps.markets1.urls'), name="markets1"),
    url(r'^2/', include('apps.markets2.urls'), name="markets2"),
    url(r'^3/', include('apps.markets3.urls'), name="markets3"),
    url(r'^contact/', include('apps.contact.urls'), name="contact"),
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomepageView.as_view(), name='homepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
