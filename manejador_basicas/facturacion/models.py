from django.db import models

# Create your models here.
class Factura(models.Model):
    nombre_factura = models.CharField(max_length=20)