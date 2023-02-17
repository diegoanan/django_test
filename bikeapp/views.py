import requests
from django.shortcuts import render
from .models import BikeStation
from django.http import HttpResponse

# Función para obtener los datos de una página
def update_bike_data(request):
    # Realizar el request get para obtener la data
    response = requests.get("http://api.citybik.es/v2/networks/bikesantiago")
    
    # Crea un json en memoria para almacenar la data en memoria en una nueva variable
    bike_data = response.json()
    stations = bike_data["network"]["stations"]

    # Recorre la data del arreglo
    for station in stations:
        #almacenala data en la DB con ayuda de objetos del modelo
        BikeStation.objects.update_or_create(
            name=station["name"],
            defaults={
                "latitude": station["latitude"],
                "longitude": station["longitude"],
                "free_bikes": station["free_bikes"],
                "empty_slots": station["empty_slots"]
            }
        )
    #Generacion de menu de retorno
    menu_html = """
    <h1>Bike-data is done!</h1>
    <h2>Menú de opciones</h2>
    <ul>
        <li><a href="http://127.0.0.1:8000">Home</a></li>
        <li><a href="http://127.0.0.1:8000/admin">Admin</a></li>
        <li><a href="http://127.0.0.1:8000/sea">Sea data update</a></li>
        <li><a href="http://127.0.0.1:8000/bike_list">Bike list</a></li>
        <li><a href="http://127.0.0.1:8000/sea_list">Sea list</a></li>
    </ul>
    """
    return HttpResponse(menu_html)

#funcion de menu principal
def menu(request):
    menu_html = """
        <h1>Menú de opciones</h1>
        <ul>
            <li><a href="http://127.0.0.1:8000/admin">Admin</a></li>
            <li><a href="http://127.0.0.1:8000/bike_list">Bike list</a></li>
            <li><a href="http://127.0.0.1:8000/bike">Bike data update</a></li>
            <li><a href="http://127.0.0.1:8000/sea_list">Sea list</a></li>
            <li><a href="http://127.0.0.1:8000/sea">Sea data update</a></li>
        </ul>
    """
    return HttpResponse(menu_html)

#Genera visualizacion de datos en html
def bike_list(request):
    bikes = BikeStation.objects.all()
    return render(request, 'bike_list.html', {'bikes': bikes})