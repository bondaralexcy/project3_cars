# Generated by Django 4.2.14 on 2024-07-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0006_car_owner_moto_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="amount",
            field=models.IntegerField(default=1000, verbose_name="цена"),
        ),
    ]
