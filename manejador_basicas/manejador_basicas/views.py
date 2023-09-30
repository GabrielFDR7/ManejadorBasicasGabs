from django.shortcuts import render

def index(request):
    return render(request, 'manejador_basicas/templates/index.html')