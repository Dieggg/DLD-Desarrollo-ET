from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.

class Region(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Tienda(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    sucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, default='En proceso', blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    costo_presupuestado = models.PositiveIntegerField(default=0, null=False,blank=False)
    costo_real = models.PositiveIntegerField(validators=[MinValueValidator(3)], default=0)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=False, blank=False)
    notas = models.TextField(max_length=800,null=False,blank=False)

    def __str__(self):
        return self.nombre if self.nombre else ''
    

class Compra(models.Model):
    nombre = models.CharField(max_length=50)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False, blank=False, editable=True)
    
    estado_compra= (
        (1,"Comprado"),
        (2,"No comprado"),
    )
    comprado = models.IntegerField(choices=estado_compra, default=2)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre



