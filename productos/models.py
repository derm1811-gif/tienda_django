from django.db import models

# Create your models here.

class Producto(models.Model):
    
    nombre=models.CharField(max_length=100)
    categoria=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    cantidad=models.IntegerField()
    estado=models.BooleanField(default=False)
