from django import forms
from .models import Contrato, Servicio, Factura


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = [
            'nombre_servicio',
            'descripcion'
        ]

        labels = {
            'nombre_servicio' : 'Nombre_servicio',
            'descripcion': 'Descripcion'
        }