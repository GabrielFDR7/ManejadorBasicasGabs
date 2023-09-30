from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import FacturaForm

pacientes = {'1010248723' : [('Tomografía', 10000), ('Radiografia', 150000)]} 

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            nuevo_Factura = form.save()
            generar_factura(nuevo_Factura)
            return render(request, 'facturacion/templates/resultado_consulta.html', {'resultado': nuevo_Factura})
    else:
        form = FacturaForm()

    return render(request, 'crear_factura.html', {'form': form})

def generar_factura(factura):

    for servicio in pacientes[(factura.id_factura)]:
        factura.servicios_y_precios.append([servicio[0], servicio[1]])
        factura.precio_total += servicio[1]
    