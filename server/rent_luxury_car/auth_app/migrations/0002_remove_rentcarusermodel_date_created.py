# Generated by Django 4.0.4 on 2022-04-28 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentcarusermodel',
            name='date_created',
        ),
    ]