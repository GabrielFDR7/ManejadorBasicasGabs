from django import forms
from .models import Factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['nombre_factura']
        labels = {
            'nombre_factura': 'ID Paciente'
        }