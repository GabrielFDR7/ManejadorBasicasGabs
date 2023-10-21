from django.db import models

class Variable(models.Model):
    # ID automático de la variable
    id = models.AutoField(primary_key=True)

    # Valor del ritmo cardíaco
    heart_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Variable ID: {self.id}, Ritmo Cardíaco: {self.heart_rate}'
