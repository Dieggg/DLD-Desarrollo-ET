from django.urls import path, include
from django.conf.urls import  url

from . import views
from compras.views import ComprasNew,ComprasEdit,ComprasDel, Panel, TiendaDel,TiendaEdit,TiendaNew,TiendaView, ProductoView,ProductoNew,ProductoEdit,ProductoDel,ListaComprasView

from registro import views as v

urlpatterns = [
    path('', views.index, name='index'), #ruta de inicio que se abré cuando carga el navegador
    path('listado',ListaComprasView.as_view(),name="listado"), #ruta para listar el listado de compras
    path('compras/create', ComprasNew.as_view(),name="create_compra"),
    path('compras/edit/<int:pk>', ComprasEdit.as_view(),name="edit_compra"),
    path('compras/delete/<int:pk>', ComprasDel.as_view(),name="delete_compra"),

    #rutas para registro y creación de cuentas.
    path('registro/',v.registro, name="registro"),
    path('',include("django.contrib.auth.urls")),

    path('panel',Panel.as_view(template_name="compras/panel.html"),name="panel"),

    path('tiendas',TiendaView.as_view(),name="tiendas"), #ruta para listar el listado de compras
    path('tiendas/create', TiendaNew.as_view(),name="create_tiendas"),
    path('tiendas/edit/<int:pk>', TiendaEdit.as_view(),name="edit_tiendas"),
    path('tiendas/delete/<int:pk>', TiendaDel.as_view(),name="delete_tiendas"),

    path('productos',ProductoView.as_view(),name="productos"), #ruta para listar el listado de compras
    path('productos/create', ProductoNew.as_view(),name="create_productos"),
    path('productos/edit/<int:pk>', ProductoEdit.as_view(template_name="productos/edit_productos.html"),name="edit_productos"),
    path('productos/delete/<int:pk>', ProductoDel.as_view(),name="delete_productos"),

]