# ---------------django_test
Proyecto realizado en un anviente virtual
En caso de tener dudas de como se crea este, se puede consultar el siguiente link: https://noemioocc.github.io/posts/Como-crear-entornos-virtuales-para-python-en-Ubunt-virtualenv/

Las librerias necesarias estan en el archivo requirements.txt se pueden instalar con ayuda del siquiente comando:
pip install -r requirements.txt 


# Ejecucion
Bastara con correr la siguiente linea de comandos

### python manage.py runserver

la visualizacion del proyecto es atraves de rireccion 127.0.0.1:8000, estos parametros son predeterminados de django

# -------------PostgreSQl
####Los parametrso necesarios en postgres son los siguientes:
en esta prueba se uso la configuracion de encryptacion md5
###creacion de la db
CREATE DATABASE djangodb;

###creacion del usuario
CREATE USER userdjango WITH PASSWORD 'djangopword123';

###Dando privilegios a usuario sobre la db
GRANT ALL PRIVILEGES ON DATABASE djangodb TO userdjango;
\c djangodb;
GRANT ALL ON SCHEMA public TO userdjango ;
GRANT ALL ON SCHEMA public TO public;
--------- Configuracion Django

### Modificacion de parametos en test_dja/settings.py DATABASES

# Creacion de app  tarea1 
python manage.py startapp bikeapp

### *creacion de modelo dentro de bikeapp/models.py
### *creacion de vista en bikeapp/views.py para obtener datos de la API y guardarlos con models
### *Creaciond de html de visualizacion para visualizacion de datos


# Creacion de app  tarea 2 
python manage.py startapp sea_search

### *creacion de modelo dentro de sea_search/models.py
### *creacion de vista en sea_search/views.py para obtener datos de la API y guardarlos con models
### *Configuracion de sea_search/admin.py
### *Creaciond de html de visualizacion para visualizacion de datos
### *configuracion de urls en test_dja/urls.py

### Creacion de  usuario y contraseña Django
se configuro parala pagina admin muestre en admin/

python manage.py createsuperuser

este usuario es de muesta, pueden ser datos aleatorios
    user:admin email: bjhf@web.mx pwd: djangopword123

### En home (localhost:8000/) se muestra menu de direcciones