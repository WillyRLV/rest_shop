from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cantidad = models.CharField(max_length=45, blank=True, null=True)
    categoria = models.CharField(max_length=45, blank=True, null=True)
    producto_img = CloudinaryField('image', default='')
    
    def __str__(self):
            return self.nombre

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)

    def __str__(self):
            return self.nombre


class Carrito(models.Model):
    idcarrito = models.AutoField(primary_key=True)  
    cantidad = models.IntegerField(blank=True, null=True)
    

    def __str__(self):
            return self.cantidad  

class Pedido(models.Model):
    idpedido = models.AutoField(db_column='idPedido', primary_key=True) 
    fecha_pedido = models.CharField(db_column='fecha-pedido', max_length=45) 
    direccion_entrega = models.CharField(db_column='direccion-entrega', max_length=45) 
    
    def __str__(self):
            return self.fecha_pedido



class CuentaAdmin(models.Model):
    idcuenta = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self):
            return self.admin 

class Entrega(models.Model):
    identrega = models.AutoField(primary_key=True)
    fecha_entrega = models.DateField(db_column='fecha-entrega', blank=True, null=True)  
    
    
    def __str__(self):
            return self.entrega 





