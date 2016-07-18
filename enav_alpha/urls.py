from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from apps.homepage.views import ProductChoiceView, RegionChoiceView

urlpatterns = [
    url(r'^markets/', include('apps.markets.urls'), name="markets"),
    url(r'^admin/', admin.site.urls),
    url(r'^$', RegionChoiceView.as_view(), name='region-choice'),
    url(r'^step-two$', ProductChoiceView.as_view(), name='product-choice'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
