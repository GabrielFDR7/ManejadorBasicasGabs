from django.shortcuts import redirect, render
from .forms import ServicioForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.factura_logic import create_servicio, get_servicio

def servicio_list(request):
    servicios = get_servicio()  # Obtén la lista actualizada de servicios
    context = {
        'servicio_list': servicios
    }
    print(servicios)
    return render(request, 'servicios.html', context)


def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            create_servicio(form)
            messages.success(request, 'Servicio creado exitosamente')
            return redirect('servicios')  # Redirige a la vista de lista de servicios
        else:
            print(form.errors)
    else:
        form = ServicioForm()

    context = {
        'form': form,
    }
    print(servicio_list)
    return render(request, 'crear_servicio.html', context)

def home(request):
    # Aquí puedes colocar el código que deseas ejecutar cuando se visite la página de inicio
    return render(request, 'manejador_basicas/templates/home.html')
# Create your views here.
