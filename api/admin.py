from django.contrib import admin

# Register your models here.
from .models import Producto, Cliente, Material, Funcion 




admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Material)
admin.site.register(Funcion)




# Carrito, Cliente, CuentaAdmin, Entrega, Pedido
# admin.site.register(Carrito)

# admin.site.register(CuentaAdmin)
# admin.site.register(Entrega)
# admin.site.register(Pedido)
