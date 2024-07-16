from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import HouseViewSet


router = DefaultRouter()
router.register('house', HouseViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
