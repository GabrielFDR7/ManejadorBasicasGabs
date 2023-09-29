from django.shortcuts import render
from .forms import ServicioForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.factura_logic import create_servicio, get_servicio

def servicio_list(request):
    servicios = get_servicio()
    context = {
        'servicio_list': servicios
    }
    return render(request, 'servicios.html', context)

def servicio_create(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            create_servicio(form)
            messages.add_message(request, messages.SUCCESS, 'Servicio create successful')
            return HttpResponseRedirect(reverse('ServicioCreate'))
        else:
            print(form.errors)
    else:
        form = ServicioForm()

    context = {
        'form': form,
    }

    return render(request, 'servicioCreate.html', context)

def home(request):
    # Aquí puedes colocar el código que deseas ejecutar cuando se visite la página de inicio
    return render(request, 'manejador_basicas/templates/home.html')
# Create your views here.
