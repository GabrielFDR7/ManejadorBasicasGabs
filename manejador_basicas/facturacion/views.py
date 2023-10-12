from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from facturacion.models import Paciente, EstadoCuenta, Servicio, Manual_Tarifario, Contrato


def crear_factura(request, id_paciente):
    try:
        paciente = Paciente.objects.get(id=id_paciente)
        servicios = EstadoCuenta.objects.filter(id_paciente=paciente).values('id_servicio')

        factura = []

        precio_total = 0

        for servicio in servicios:
            manual_tarifario = Manual_Tarifario.objects.get(id_servicio=servicio['id_servicio'], id_contrato=paciente.id_contrato)
            servicio = Servicio.objects.get(id=servicio['id_servicio'])

            precio = manual_tarifario.precio
            factura.append((servicio, precio))
            precio_total += precio

        return JsonResponse({'precios_servicios': factura}, {'precio_total': precio_total})

    except Paciente.DoesNotExist:
        return JsonResponse({'error': 'Paciente no encontrado'}, status=404)



    
    