from django.shortcuts import render, redirect, get_object_or_404
from .models import Compra, Producto, Tienda
from django.contrib.auth.models import User
from .forms import TiendaForm,ProductoForm, CompraForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request,'compras/index.html')

class ListaComprasView(generic.ListView):
    model = Compra
    template_name = "compras/listado_compras.html"
    context_object_name = "obj"
    #queryset = Compra.objects.filter(user=user.id)
    
    # def get_queryset(self):
    #     return Compra.objects.filter(usuario=self.request.user)

class ComprasNew(generic.CreateView):
    model = Compra
    template_name="compras/create_compras.html"
    context_object_name = 'obj'
    form_class = CompraForm
    success_url =  reverse_lazy('listado')

class ComprasEdit(generic.UpdateView):
    model = Compra
    template_name="compras/create_compras.html"
    context_object_name = 'obj'
    form_class = CompraForm
    success_url =  reverse_lazy('listado')

class ComprasDel(generic.DeleteView):
    model = Compra
    template_name="compras/delete_compras.html"
    context_object_name = 'obj'
    success_url =  reverse_lazy('listado')

class Panel(generic.TemplateView):
    template_name='compras/panel'

class TiendaView(generic.ListView):
    model = Tienda
    template_name = "tiendas/listado_tiendas.html"
    context_object_name = "obj"

class TiendaNew(generic.CreateView):
    model = Tienda
    template_name="tiendas/create_tiendas.html"
    context_object_name = 'obj'
    form_class = TiendaForm
    success_url =  reverse_lazy('tiendas')

class TiendaEdit(generic.UpdateView):
    model = Tienda
    template_name="tiendas/create_tiendas.html"
    context_object_name = 'obj'
    form_class = TiendaForm
    success_url =  reverse_lazy('tiendas')

class TiendaDel(generic.DeleteView):
    model = Tienda
    template_name="tiendas/delete_tiendas.html"
    context_object_name = 'obj'
    success_url =  reverse_lazy('tiendas')


class ProductoView(generic.ListView):
    model = Producto
    template_name = "productos/listado_productos.html"
    context_object_name = "obj"

class ProductoNew(generic.CreateView):
    model = Producto
    template_name="productos/create_productos.html"
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url =  reverse_lazy('productos')

class ProductoEdit(generic.UpdateView):
    model = Producto
    template_name="productos/create_productos.html"
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url =  reverse_lazy('productos')

class ProductoDel(generic.DeleteView):
    model = Producto
    template_name="productos/delete_productos.html"
    context_object_name = 'obj'
    success_url =  reverse_lazy('productos')

