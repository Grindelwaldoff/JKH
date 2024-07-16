# Generated by Django 5.0.7 on 2024-07-15 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(help_text='укажите адрес дома', max_length=255, verbose_name='Адрес:')),
                ('name', models.CharField(help_text='укажите название дома', max_length=255, unique=True, verbose_name='Название:')),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='укажите название тарифа', max_length=255, verbose_name='Название:')),
                ('price_per_unit', models.PositiveSmallIntegerField(help_text='укажите стоимость в рублях за единицу ресурса', verbose_name='Стоимость:')),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(help_text='укажите номер квартиры', verbose_name='Номер квартиры:')),
                ('area', models.PositiveSmallIntegerField(help_text='укажите площадь квартиры в квадратных метрах', verbose_name='Площадь квартиры:')),
                ('house', models.ForeignKey(help_text='укажите дом, в котором находится квартира', on_delete=django.db.models.deletion.CASCADE, related_name='apartments', to='infrastructure.house', verbose_name='Дом:')),
            ],
        ),
        migrations.CreateModel(
            name='WaterMeter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(help_text='укажите серийный номер счетчика', max_length=255, unique=True, verbose_name='Серийный номер:')),
                ('apartment', models.ForeignKey(help_text='укажите квартиру, в которой установлен счетчик', on_delete=django.db.models.deletion.CASCADE, related_name='water_meters', to='infrastructure.apartment', verbose_name='Квартира:')),
            ],
        ),
        migrations.CreateModel(
            name='WaterMeterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading_date', models.DateField(help_text='укажите дату снятия показания', verbose_name='Дата показания:')),
                ('reading_value', models.PositiveIntegerField(help_text='укажите значение показания счетчика', verbose_name='Показание:')),
                ('water_meter', models.ForeignKey(help_text='укажите счетчик, для которого вводятся показания', on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='infrastructure.watermeter', verbose_name='Счетчик:')),
            ],
            options={
                'unique_together': {('water_meter', 'reading_date')},
            },
        ),
    ]