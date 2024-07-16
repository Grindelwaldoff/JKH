from django.contrib import admin

from infrastructure.models import (
    House,
    Tariff,
    Apartment,
    WaterMeter,
    WaterMeterData,
)


admin.site.register(House)
admin.site.register(Apartment)
admin.site.register(Tariff)
admin.site.register(WaterMeter)
admin.site.register(WaterMeterData)
