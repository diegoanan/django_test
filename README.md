# django_test


# -------------PostgreSQl
Los parametrso necesarios en postgres son los siguientes:
# en esta prueba se uso la configuracion de encryptacion md5
creacion de la db
# CREATE DATABASE djangodb;

creacion del usuario
# CREATE USER userdjango WITH PASSWORD 'djangopword123';

Dando privilegios a usuario sobre la db
# GRANT ALL PRIVILEGES ON DATABASE djangodb TO userdjango;
# \c djangodb;
# GRANT ALL ON SCHEMA public TO userdjango ;
# GRANT ALL ON SCHEMA public TO public;
--------- Configuracion Django

# Modificacion de parametos en test_dja/settings.py DATABASES

Creacion de app con
# python manage.py startapp bikeapp

## creacion de modelo dentro de bikeapp/models.py

## creacion de vista en bikeapp/views.py para obtener datos de la API y guardarlos con models

## creacion y configuracion de URL en bikeapp/urls.py

## configuracion de url en test_dja/urls.py