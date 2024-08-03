from rest_framework import serializers
import re

from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"

    def validate_flightNumber(self, flightNumber):
        if re.match("^[a-zA-Z0-9]*$", flightNumber) == None:
            raise serializers.ValidationError("Please enter alpha numberic value")
        return flightNumber

    def validate(self, data):
        print("THIS IS DATA", data)

        return data

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
