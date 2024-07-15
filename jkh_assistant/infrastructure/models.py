from django.db import models
from django.conf import settings


class House(models.Model):
    """Модель Дома."""

    address = models.CharField(
        max_length=settings.MAX_STR_LENGTH,
        verbose_name="Адрес:",
        help_text="укажите адрес дома"
    )
    name = models.CharField(
        max_length=settings.MAX_STR_LENGTH,
        unique=True,
        verbose_name="Название:",
        help_text="укажите название дома"
    )

    def __str__(self):
        return f"{self.name} ({self.address})"


class Apartment(models.Model):
    """Модель квартир."""

    house = models.ForeignKey(
        House,
        related_name="apartments",
        on_delete=models.CASCADE,
        verbose_name="Дом:",
        help_text="укажите дом, в котором находится квартира"
    )
    number = models.PositiveSmallIntegerField(
        verbose_name="Номер квартиры:",
        help_text="укажите номер квартиры"
    )
    area = models.PositiveSmallIntegerField(
        verbose_name="Площадь квартиры:",
        help_text="укажите площадь квартиры в квадратных метрах"
    )

    def __str__(self):
        return f"{self.house.address} {self.number}"


class WaterMeter(models.Model):
    """Модель счетчиков."""

    apartment = models.ForeignKey(
        Apartment,
        related_name="water_meters",
        on_delete=models.CASCADE,
        verbose_name="Квартира:",
        help_text="укажите квартиру, в которой установлен счетчик"
    )
    serial_number = models.CharField(
        max_length=settings.MAX_STR_LENGTH,
        unique=True,
        verbose_name="Серийный номер:",
        help_text="укажите серийный номер счетчика"
    )

    def __str__(self):
        return self.serial_number


class WaterMeterData(models.Model):
    """Модель данных для каждого счетчика."""

    water_meter = models.ForeignKey(
        WaterMeter,
        related_name="readings",
        on_delete=models.CASCADE,
        verbose_name="Счетчик:",
        help_text="укажите счетчик, для которого вводятся показания"
    )
    reading_date = models.DateField(
        verbose_name="Дата показания:",
        help_text="укажите дату снятия показания"
    )
    reading_value = models.PositiveIntegerField(
        verbose_name="Показание:",
        help_text="укажите значение показания счетчика"
    )

    class Meta:
        unique_together = ("water_meter", "reading_date")

    def __str__(self):
        return f"{self.water_meter.serial_number} / {self.reading_date}"


class Tariff(models.Model):
    """Модель тарифа."""

    name = models.CharField(
        max_length=settings.MAX_STR_LENGTH,
        verbose_name="Название:",
        help_text="укажите название тарифа"
    )
    price_per_unit = models.PositiveSmallIntegerField(
        verbose_name="Стоимость:",
        help_text="укажите стоимость в рублях за единицу ресурса"
    )

    def __str__(self):
        return self.name