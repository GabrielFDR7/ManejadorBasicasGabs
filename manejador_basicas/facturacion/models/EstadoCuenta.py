from django.db import models
from facturacion.models.Paciente import Paciente
from facturacion.models.Servicio import Servicio

###Tabla Estado de Cuenta
class EstadoCuenta(models.Model):
    id_paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    id_servicio = models.OneToOneField(Servicio, on_delete=models.CASCADE)

