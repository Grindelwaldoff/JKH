from celery.result import AsyncResult
from rest_framework.status import HTTP_200_OK, HTTP_202_ACCEPTED
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action

from api.tasks import bills_calculation
from api.serializers import (
    HouseSerializer,
    ApartmentSerializer,
    WaterMeterSerializer,
    WaterMeterDataSerializer,
)
from infrastructure.models import (
    House,
    Apartment,
    WaterMeter,
    WaterMeterData,
)


class HouseViewSet(ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class ApartmentViewSet(ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

    def perform_create(self, serializer):
        serializer.save(
            house=House.objects.get(id=self.request.data.get("house"))
        )


class WaterMeterViewSet(ModelViewSet):
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterSerializer

    def perform_create(self, serializer):
        serializer.save(
            apartment=Apartment.objects.get(
                id=self.request.data.get("apartment")
            )
        )


class WaterMeterDataViewSet(ModelViewSet):
    queryset = WaterMeterData.objects.all()
    serializer_class = WaterMeterDataSerializer

    def perform_create(self, serializer):
        serializer.save(
            water_meter=WaterMeter.objects.get(
                id=self.request.data.get("water_meter")
            )
        )


class TaskView(ViewSet):

    @action(["post"], detail=False)
    def create_task(self, request, *args, **kwargs):
        rent_task = bills_calculation.apply_async()
        return Response(
            {"task_id": rent_task.id}, status=HTTP_202_ACCEPTED
        )

    @action(["get"], detail=True)
    def get_result(self, request, pk=None):
        result = AsyncResult(pk)
        match result.state:
            case "PENDING":
                response = {"state": result.state, "status": "Pending..."}
            case "FAILURE":
                response = {"state": result.state, "result": result.result}
            case _:
                print(result.info)
                response = result.info

        return Response(response, status=HTTP_200_OK)
