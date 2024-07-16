import factory
from factory import fuzzy
from datetime import datetime, timedelta
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
    name = factory.Faker("name")


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

    value = factory.LazyAttribute(
        lambda o: WaterMeterDataFactory._generate_value()
    )
    date = factory.LazyAttribute(
        lambda o: WaterMeterDataFactory._generate_date()
    )
    water_meter = factory.SubFactory(WaterMeterFactory)

    @staticmethod
    def _generate_value():
        return fuzzy.FuzzyInteger(1000, 10000).fuzz()

    @staticmethod
    def _generate_date():
        today = datetime.now()
        months_ago = fuzzy.FuzzyInteger(1, 12).fuzz()
        past_date = today - timedelta(days=months_ago * 30)
        return past_date.strftime("%Y-%m-%d")

    @factory.post_generation
    def set_previous_values(self, create, extracted, **kwargs):
        if extracted:
            previous_data = []
            for i in range(extracted):
                past_date = self.date - timedelta(days=(i + 1) * 30)
                previous_data.append(
                    WaterMeterData(
                        water_meter=self.water_meter,
                        value=self.value - (i + 1) * 100,
                        date=past_date,
                    )
                )
            WaterMeterData.objects.bulk_create(previous_data)


class TariffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tariff

    name = factory.Faker("word")
    price_per_unit = factory.Faker("random_int", min=1, max=100)
