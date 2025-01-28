from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

# Create your models here.

class Laboratorio(models.Model):    
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, default='Santiago')
    pais = models.CharField(max_length=100, default='Chile')
    
    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100, default='Qumico Farmaceutico')
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)
    
    def clean(self):
        if self.f_fabricacion.year < 2015:
            raise ValidationError('La fecha de fabricacion debe ser posterior a 2015')
            
    def __str__(self):
        return self.nombre