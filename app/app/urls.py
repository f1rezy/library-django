from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from core.views import UserViewSet
from feedback.views import FeedbackViewSet, OfferViewSet
from library.views import BookViewSet, ReservationViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'reservations', ReservationViewSet, basename='reservations')
router.register(r'feedbacks', FeedbackViewSet, basename='feedbacks')
router.register(r'offers', OfferViewSet, basename='offers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/profile/', UserViewSet.as_view(), name='profile'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT,
        )
    urlpatterns += staticfiles_urlpatterns()
