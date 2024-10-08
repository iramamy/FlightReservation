from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Flight, Reservation, Passenger
from .serializers import FlightSerializer, ReservationSerializer, PassengerSerializer


@api_view(["POST"])
def find_flights(request):
    flight = Flight.objects.filter(
        departureCity=request.data["departureCity"],
        ArrivalCity=request.data["ArrivalCity"],
        dateOfDeparture=request.data["dateOfDeparture"],
    )
    serializer = FlightSerializer(flight, many=True)

    return Response(serializer.data)


@api_view(["POST"])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data["flightId"])
    passenger = Passenger()
    passenger.firstName = request.data["firstName"]
    passenger.lastName = request.data["lastName"]
    passenger.middleName = request.data["middleName"]
    passenger.email = request.data["email"]
    passenger.phone = request.data["phone"]

    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)


class FligthViewSets(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)


class PassengerViewSets(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSets(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
