# Generated by Django 4.0.4 on 2022-05-01 19:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_year_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year_created',
            field=models.IntegerField(default=2000, validators=[django.core.validators.MaxValueValidator(2022), django.core.validators.MinValueValidator(2000)]),
        ),
    ]
