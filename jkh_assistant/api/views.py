from rest_framework.viewsets import ModelViewSet

from api.serializers import HouseSerializer
from infrastructure.models import (
    House,
    Tariff,
    Apartment,
    WaterMeter,
    WaterMeterData,
)


class HouseViewSet(ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
