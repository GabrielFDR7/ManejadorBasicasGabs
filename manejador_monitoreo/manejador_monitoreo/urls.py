from django.urls import path
from . import views


urlpatterns = [
    path('measurements/', views.measurement_list, name='measurementList'),
    path('measurements/create/', views.measurement_create, name='measurementCreate'),
]

