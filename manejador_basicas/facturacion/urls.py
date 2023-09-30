from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from facturacion import views

urlpatterns = [
    path('servicios/', views.servicio_list, name='servicios'),
    path('crearServicio/', views.servicio_create, name='servicioCreate'),
    # Otras rutas aquí...
]
