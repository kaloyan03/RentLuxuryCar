# Generated by Django 4.0.4 on 2022-04-29 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
    ]
