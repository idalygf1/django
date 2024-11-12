
# Register your models here.

from django.contrib import admin
from .models import Producto, Pedido


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'stock')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('precio',)
    ordering = ('nombre',)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'cantidad', 'subtotal', 'nombre_cliente', 'fecha')
    search_fields = ('nombre_cliente', 'producto__nombre')
    list_filter = ('fecha',)
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)