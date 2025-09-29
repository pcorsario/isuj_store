from django.contrib import admin
from .models import Producto, Categoria
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')
    search_fields = ('nombre', 'categoria')
    list_filter = ('categoria',)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)