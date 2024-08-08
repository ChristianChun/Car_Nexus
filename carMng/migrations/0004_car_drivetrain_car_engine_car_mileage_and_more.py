# Generated by Django 5.0.6 on 2024-05-18 10:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carMng", "0003_car_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="drivetrain",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="car",
            name="engine",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="car",
            name="mileage",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="car",
            name="transmission",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
