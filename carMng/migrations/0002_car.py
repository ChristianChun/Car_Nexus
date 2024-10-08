# Generated by Django 5.0.6 on 2024-05-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carMng", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("make", models.CharField(max_length=200)),
                ("model", models.CharField(max_length=200)),
                ("year", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("publishdate", models.DateField(auto_now_add=True)),
                ("description", models.TextField()),
                ("picture", models.FileField(upload_to="carProject/static/uploads")),
                (
                    "pic_path",
                    models.CharField(blank=True, editable=False, max_length=300),
                ),
            ],
        ),
    ]
