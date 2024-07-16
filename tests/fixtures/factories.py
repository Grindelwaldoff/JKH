import factory
from infrastructure.models import (
    House,
    Apartment,
    WaterMeter,
    WaterMeterData,
    Tariff,
)


class HouseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = House

    address = factory.Faker("address")
    name = factory.Faker("word")


class ApartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Apartment

    house = factory.SubFactory(HouseFactory)
    number = factory.Sequence(lambda n: n + 1)
    area = factory.Faker("random_int", min=30, max=200)


class WaterMeterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WaterMeter

    apartment = factory.SubFactory(ApartmentFactory)
    serial_number = factory.Faker("ean13")


class WaterMeterDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WaterMeterData

    date = factory.Faker("date")
    value = factory.Faker("pyfloat", positive=True, min_value=1, max_value=10000)
    water_meter = factory.SubFactory(WaterMeterFactory)


class TariffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tariff

    name = factory.Faker("word")
    price_per_unit = factory.Faker("random_int", min=1, max=100)
