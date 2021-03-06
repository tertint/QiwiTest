from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('service_orders.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
