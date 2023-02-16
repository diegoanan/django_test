import requests
from .models import BikeStation
from django.http import HttpResponse
from django.shortcuts import render

def update_bike_data(request):
    response = requests.get("http://api.citybik.es/v2/networks/bikesantiago")
    bike_data = response.json()
    stations = bike_data["network"]["stations"]
    for station in stations:
        BikeStation.objects.update_or_create(
            name=station["name"],
            defaults={
                "latitude": station["latitude"],
                "longitude": station["longitude"],
                "free_bikes": station["free_bikes"],
                "empty_slots": station["empty_slots"]
            }
        )
    return HttpResponse("Bike-data is done!")

