from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Material (models.Model):
    nombre = models.CharField(max_length= 200)
    pubdate = models.DateField (auto_now_add= True)
    def __str__(self):
            return self.nombre

class Funcion (models.Model):
    nombre = models.CharField(max_length= 200)
    pubdate = models.DateField (auto_now_add= True)
    def __str__(self):
            return self.nombre

class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cantidad = models.IntegerField(default=0)
    material = models.ForeignKey (Material, on_delete=models.RESTRICT)
    funcion = models.ForeignKey (Funcion, on_delete=models.RESTRICT)
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

# class Carrito(models.Model):
#     idcarrito = models.AutoField(primary_key=True)  
#     cantidad = models.IntegerField(blank=True, null=True)
#     cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT, null=True)
#     producto = models.ForeignKey(Producto,on_delete=models.RESTRICT, null=True)

#     def __str__(self):
#             return self.cantidad  

# class Pedido(models.Model):
#     idpedido = models.AutoField(primary_key=True) 
#     fecha_pedido = models.CharField(max_length=45) 
#     direccion_entrega = models.CharField(max_length=45) 
    
#     def __str__(self):
#             return self.fecha_pedido

# class CuentaAdmin(models.Model):
#     idcuenta = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=45)
#     password = models.CharField(max_length=45)

#     def __str__(self):
#             return self.admin 

# class Entrega(models.Model):
#     identrega = models.AutoField(primary_key=True)
#     fecha_entrega = models.DateField(default='', null=False) 
    
    
#     def __str__(self):
#             return self.fecha_entrega 
