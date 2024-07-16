from celery import shared_task

from infrastructure.models import (
    House,
    Tariff,
    Apartment,
    WaterMeter,
    CalculationResults,
)


def calculate_water_meters_values(apartment: Apartment, tariff: Tariff):
    result = 0
    for water_meter in WaterMeter.objects.filter(apartment=apartment.id):
        if len(water_meter.readings.all()) >= 2:
            water_meter_readings = water_meter.readings.all().order_by(
                "-date"
            )[:3]
            print(water_meter_readings)
            result += tariff.price_per_unit * (
                water_meter_readings[0].value - water_meter_readings[1].value
            )
    CalculationResults.objects.get_or_create(
        apartment=apartment, result=result, type="water_meter"
    )
    return result


@shared_task
def bills_calculation():
    # подсчет всех показателей счетчиков для каждого дома
    print(Tariff.objects.all())
    rent_tariff, meter_tariff = Tariff.objects.all()
    result = []
    for apartment in Apartment.objects.all():
        rent = apartment.area * rent_tariff.price_per_unit
        meter = calculate_water_meters_values(apartment, meter_tariff)
        CalculationResults.objects.get_or_create(
            apartment=apartment, result=rent, type="rent"
        )
        result.append(
            {
                "apartment_number": apartment.number,
                "bill": rent + meter,
            }
        )
    return result
