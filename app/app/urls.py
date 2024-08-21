from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from rest_framework import routers

# from repairs.views import ImageViewSet, RepairViewSet
# from tablets.views import TabletViewSet

router = routers.DefaultRouter()
# router.register(r'tablets', TabletViewSet)
# router.register(r'repairs', RepairViewSet)
# router.register(r'images', ImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT,
        )
    urlpatterns += staticfiles_urlpatterns()
