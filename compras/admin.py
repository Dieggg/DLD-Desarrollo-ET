from django.contrib import admin
from .models import Region, Ciudad, Producto, Tienda, Compra

# Register your models here.

admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Producto)
admin.site.register(Tienda)
admin.site.register(Compra)

