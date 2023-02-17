import json
import requests
from django.http import HttpResponse
from bs4 import BeautifulSoup
from .models import Proyecto
import datetime

# URL de la página a scrapear
url = 'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php'

# Configuración de headers para evitar problemas con el servidor
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php',
    'Connection': 'keep-alive'
}

# Función para obtener los datos de una página
def obtener_datos_pagina(num_pagina):
    # Parámetros para enviar en el request POST
    params = {'pagina': num_pagina, 'resultados_por_pagina': 100}
    # Realizar el request POST con los parámetros y headers
    r = requests.post(url, data=params, headers=headers)

    # Obtener el contenido HTML de la página
    soup = BeautifulSoup(r.content, 'html.parser')

    # Encontrar la tabla que contiene los datos
    tabla = soup.find('table', {'class': 'tabla_datos'})
    # Obtener los datos de la tabla y guardarlos en la base de datos
    if tabla is not None:
        for fila in tabla.find_all('tr')[2:]:
            try:
                datos = fila.find_all('td')
            except:
                continue
            nombre = datos[1].text.strip()
            #nos ayudamos de date time para hacer un case a la variable fecha
            fecha = datetime.datetime.strptime(str(datos[7].text.strip()),"%d/%m/%Y").strftime("%Y-%m-%d")
            region = datos[3].text.strip()
            tipo_proyecto = datos[2].text.strip()
            estado = datos[8].text.strip()

            proyecto = Proyecto(nombre=nombre, fecha=fecha, region=region, tipo_proyecto=tipo_proyecto, estado=estado)
            #Guardar la data en la base de datos
            proyecto.save()


#Esta funcion puede demorar en cargar
def get_data_sea(request):
    # Recorrer todas las páginas y obtener la información de las tablas(limitado a 11 paginas, se puede modificar)
    for i in range(1, 11):
        print(f'Obteniendo datos de la página {i}...')
        obtener_datos_pagina(i)

    # Obtener los datos de la base de datos y guardarlos en un archivo .json
    proyectos = Proyecto.objects.all().values()
    with open('proyectos.json', 'w') as f:
        json.dump(list(proyectos), f,default=str)
    
    menu_html = """
    <h1>Sea-data is done!</h1>
    <h2>Menú de opciones</h2>
    <ul>
        <li><a href="http://127.0.0.1:8000">Home</a></li>
        <li><a href="http://127.0.0.1:8000/admin">Admin</a></li>
        <li><a href="http://127.0.0.1:8000/bike">Bike data update</a></li>
    </ul>
    """
    #retorna menu de retorno
    return HttpResponse(menu_html)
