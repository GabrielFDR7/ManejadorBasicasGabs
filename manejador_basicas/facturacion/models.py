from django.db import models


# Create your models here.
class Factura(models.Model):
    id_factura = models.CharField(max_length=20)
    servicios_y_precios = []
    precio_total = 0
    