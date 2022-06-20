from django.contrib import admin

# Register your models here.
from .models import Producto, Carrito, Cliente, CuentaAdmin, Entrega, Pedido

admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Cliente)
admin.site.register(CuentaAdmin)
admin.site.register(Entrega)
admin.site.register(Pedido)
