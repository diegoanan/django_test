from django.urls import path
from .views import update_bike_data

urlpatterns = [
    path('views/', update_bike_data, name='update_bike_data'),
]