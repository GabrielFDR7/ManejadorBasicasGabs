from django.db import models

class Factura(models.Model):
    numero_factura = models.CharField(max_length=20)
    fecha = models.DateField()
    id_cliente = models.CharField(max_length=20)
    nombre_cliente = models.CharField(max_length=50)

    def __str__(self):
        return self.numero_factura
    
class Contrato(models.Model):
    nombre_contrato = models.CharField(max_length=20)
    servicios = {}  # Esto podría no ser necesario si quieres un diccionario de servicios por contrato

    def __str__(self):
        return self.nombre_contrato

class Servicio(models.Model):
    nombre_servicio = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre_servicio