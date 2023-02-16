from django.contrib import admin
from django.urls import path
from .views import update_bike_data

urlpatterns = [
    path('admin/',admin.site.urls),
    path('views/', update_bike_data, name='update_bike_data')
]