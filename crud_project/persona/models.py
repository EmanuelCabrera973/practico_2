from django.db import models
from oficina.models import Oficina

class Persona(models.Model):
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    oficina = models.models.ForeignKey(Oficina, on_delete=models.CASCADE, related_name = 'personas')
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    

# Create your models here.
