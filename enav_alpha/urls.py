from django.conf.urls import url, include
from django.contrib import admin
from apps.homepage.views import ProductChoiceView, RegionChoiceView

urlpatterns = [
    url(r'^markets/', include('apps.markets.urls'), name="markets"),
    url(r'^admin/', admin.site.urls),
    url(r'^$', RegionChoiceView.as_view(), name='region-choice'),
    url(r'^step-two$', ProductChoiceView.as_view(), name='product-choice'),
]
