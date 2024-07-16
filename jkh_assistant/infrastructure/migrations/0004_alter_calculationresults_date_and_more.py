# Generated by Django 5.0.7 on 2024-07-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructure', '0003_alter_watermeterdata_date_calculationresults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculationresults',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='watermeterdata',
            name='date',
            field=models.DateField(auto_now_add=True, help_text='укажите дату снятия показания', verbose_name='Дата показания:'),
        ),
    ]
