# Generated by Django 5.0.6 on 2024-05-19 04:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carMng", "0005_alter_car_drivetrain_alter_car_engine_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
    ]
