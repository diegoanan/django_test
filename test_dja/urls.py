"""test_dja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from bikeapp.views import update_bike_data,menu
from sea_search.views import get_data_sea



urlpatterns = [
    path('',menu,name='menu'),
    path('admin/',admin.site.urls),
    #Con esto ejecutamos las funciones para cargar la data a la db
    path('bike/',update_bike_data,name='update_bike_data'),
    path('sea/',get_data_sea,name='get_data_sea'),
    

]
