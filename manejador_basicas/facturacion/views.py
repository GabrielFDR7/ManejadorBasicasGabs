from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from facturacion.models.Paciente import Paciente
from facturacion.models.EstadoCuenta import EstadoCuenta
from facturacion.models.Servicio import Servicio
from facturacion.models.Manual_Tarifario import Manual_Tarifario
from facturacion.models.Contrato import Contrato
from django.core.exceptions import ObjectDoesNotExist

def crear_factura(request):
    if request.method == 'GET':
        cedula_paciente = request.GET.get('id_paciente')
        
        try:
            paciente = Paciente.objects.get(id=cedula_paciente)
            servicios = EstadoCuenta.objects.filter(id_paciente=paciente).values('id_servicio')

            factura = []
            precio_total = 0

            for servicio in servicios:
                manual_tarifario = Manual_Tarifario.objects.get(id_servicio=servicio['id_servicio'], id_contrato=paciente.id_contrato)
                servicio = Servicio.objects.get(id=servicio['id_servicio'])

                precio = manual_tarifario.precio
                factura.append((servicio, precio))
                precio_total += precio

            return render(request, 'resultado_consulta.html', {
                'resultado': {
                    'id_factura': paciente.id,  # Aquí puedes modificar el dato que deseas mostrar
                    'servicios_y_precios': factura,
                    'precio_total': precio_total
                }
            })

        except ObjectDoesNotExist:
            return render(request, 'resultado_consulta.html', {'error': 'Paciente no encontrado'})

    return HttpResponse("Algo salió mal") 

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})




