from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from api.views import (
    TaskView,
    HouseViewSet,
    ApartmentViewSet,
    WaterMeterViewSet,
    WaterMeterDataViewSet,
)


router = DefaultRouter()
router.register(r"tasks", TaskView, basename="task")
router.register("houses", HouseViewSet)
router.register("apartments", ApartmentViewSet)
router.register("water-meters/data", WaterMeterDataViewSet)
router.register("water-meters", WaterMeterViewSet)


urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api/v1/", include(router.urls)),
]
