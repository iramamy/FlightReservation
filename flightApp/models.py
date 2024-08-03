from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Flight(models.Model):
    flightNumber = models.CharField(max_length=15)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=100)
    ArrivalCity = models.CharField(max_length=100)
    dateOfDeparture = models.DateField()
    estimateTimeOfDeparture = models.TimeField()

    def __str__(self):
        return f"{self.flightNumber} - {self.operatingAirlines}"


class Passenger(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, blank=True)
    middleName = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.firstName}"


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.flight.flightNumber}: {self.passenger.firstName}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance, created, **kargs):
    if created:
        Token.objects.create(user=instance)
