from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import FacturaForm

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            nuevo_Factura = form.save()
    else:
        form = FacturaForm()

    return render(request, 'crear_factura.html', {'form': form})
