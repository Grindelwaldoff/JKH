from rest_framework import serializers

from infrastructure.models import (
    House,
    Tariff,
    Apartment,
    WaterMeter,
    WaterMeterData,
)


class WaterMeterDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = WaterMeterData
        fields = ('id', "value", "date")


class WaterMeterSerializer(serializers.ModelSerializer):
    values = WaterMeterDataSerializer(many=True, read_only=True)

    class Meta:
        model = WaterMeter
        fields = (
            'id',
            "serial_number",
            "values",
        )


class ApartmentSerializer(serializers.ModelSerializer):
    water_meters = WaterMeterSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = (
            "id",
            "number",
            "area",
            "water_meters",
        )


class HouseSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(read_only=True)

    class Meta:
        model = House
        fields = ("id", "address", "name", "apartments")
