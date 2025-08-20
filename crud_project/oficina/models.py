from django.db import models

class Oficina(models.Model):
    nombre = models.CharField(max_Length=100)
    nombre_corto = models.Charfield(max_length=10, unique=True)
    
    def __str__(self):
        return f"{self.nombre}({self.nombre_corto})"
    
# Create your models here.
