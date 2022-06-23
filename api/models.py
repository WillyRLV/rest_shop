from django.db import models
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.
class Material (models.Model):
    material_id = models.AutoField(primary_key=True)
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
    material = models.ForeignKey (Material,related_name='Productos',
                                    to_field='material_id',on_delete=models.RESTRICT,
                                    db_column='material_id',verbose_name='material')
    funcion = models.ForeignKey (Funcion, on_delete=models.RESTRICT)
    producto_img = CloudinaryField('image', default='')
    url = models.TextField()
    rango= models.CharField(max_length=50)
    dimension=models.CharField(max_length=50)
    fecha_creada=models.DateTimeField(default=datetime.now)
    
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

class CuentaAdmin(models.Model):
    idcuenta = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self):
            return self.username

class Carrito(models.Model):
    idcarrito = models.AutoField(primary_key=True)  
    cantidad = models.IntegerField(default=0)
    producto = models.ForeignKey (Producto, on_delete=models.RESTRICT)
    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)  

    def __str__(self):
            return self.producto.nombre

class Pedido(models.Model):
    idpedido = models.AutoField(primary_key=True) 
    fecha_pedido = models.DateTimeField(auto_now_add=True) 
    direccion_entrega = models.CharField(max_length=200) 
    carrito_detalle = models.ForeignKey(Carrito, on_delete=models.RESTRICT)
    
    def __str__(self):
            return self.direccion_entrega

class Entrega(models.Model):
    identrega = models.AutoField(primary_key=True)
    fecha_entrega = models.DateField(null=True, verbose_name='FechadeEntrega') 
    entrega_img = CloudinaryField('image', default='',)
    # pedido = models.ForeignKey(Pedido,on_delete=models.RESTRICT)

    # def __str__(self):
    #             return self.fecha_entrega

    # Contacto 
class Contacto (models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100) 
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()

    def __str__(self):
            return self.asunto

            