from django.db import models
from variables.models import Variable

class Measurement(models.Model):
    # ID automático de la medición
    id = models.AutoField(primary_key=True)

    # Valor de la medida
    value = models.DecimalField(max_digits=5, decimal_places=2)

    # Fecha y hora de la medida
    timestamp = models.DateTimeField(auto_now_add=True)

    # Relación muchos a uno con Variable
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE)

    # Campo para indicar si la medición es anormal
    anormal = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.anormal = self.verificarAnormalidad()
        super().save(*args, **kwargs)

    def verificarAnormalidad(self):
        return self.value > 100

    def __str__(self):
        return f'Medida ID: {self.id}, Valor: {self.value}, Fecha y Hora: {self.timestamp}, Anormal: {self.anormal}'
