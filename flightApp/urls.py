from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register("flight", views.FligthViewSets)
router.register("passenger", views.PassengerViewSets)
router.register("reservation", views.ReservationViewSets)

urlpatterns = [
    path("", include(router.urls)),
    path("find-flights/", views.find_flights, name="find_flights"),
    path("save-reservation/", views.save_reservation, name="save_reservation"),
    path("api-auth-token/", obtain_auth_token, name="api_auth_token"),
]
