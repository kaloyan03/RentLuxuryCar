# Generated by Django 4.0.4 on 2022-05-01 18:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2)])),
                ('model', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(3)])),
                ('coupe_type', models.CharField(choices=[('Hatchback', 'Hatchback'), ('Sedan', 'Sedan'), ('Family', 'Family'), ('Coupe', 'Coupe'), ('Cabriolet', 'Cabriolet')], max_length=9, validators=[django.core.validators.MinLengthValidator(5)])),
                ('fuel_type', models.CharField(choices=[('Gasoline', 'Gasoline'), ('Diesel', 'Diesel'), ('Petrol', 'Petrol'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], max_length=8, validators=[django.core.validators.MinLengthValidator(6)])),
                ('gearbox_type', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=9, validators=[django.core.validators.MinLengthValidator(6)])),
                ('fuel_consumption', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('horsepower', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1500)])),
            ],
        ),
    ]