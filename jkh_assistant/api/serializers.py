from rest_framework import serializers

from infrastructure.models import (
    House,
    Apartment,
    WaterMeter,
    WaterMeterData,
)


class WaterMeterDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = WaterMeterData
        fields = ("id", "value", "date")


class WaterMeterSerializer(serializers.ModelSerializer):
    readings = WaterMeterDataSerializer(many=True, required=False)

    class Meta:
        model = WaterMeter
        fields = (
            "id",
            "serial_number",
            "readings",
        )


class ApartmentSerializer(serializers.ModelSerializer):
    water_meters = WaterMeterSerializer(many=True, required=False)

    class Meta:
        model = Apartment
        fields = (
            "id",
            "number",
            "area",
            "water_meters",
        )


class HouseSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True, required=False)

    class Meta:
        model = House
        fields = ("id", "address", "name", "apartments")
