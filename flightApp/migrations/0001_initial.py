# Generated by Django 5.0.7 on 2024-08-01 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flight",
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
                ("flightNumber", models.CharField(max_length=15)),
                ("operatingAirlines", models.CharField(max_length=20)),
                ("departureCity", models.CharField(max_length=100)),
                ("ArrivalCity", models.CharField(max_length=100)),
                ("dateOfDeparture", models.DateField()),
                ("estimateTimeOfDeparture", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Passenger",
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
                ("firstName", models.CharField(max_length=50)),
                ("lastName", models.CharField(blank=True, max_length=50)),
                ("middleName", models.CharField(blank=True, max_length=50)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
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
                (
                    "flight",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flightApp.flight",
                    ),
                ),
                (
                    "passenger",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flightApp.passenger",
                    ),
                ),
            ],
        ),
    ]
