from django import forms
from .models import Tienda, Compra, Producto, Ciudad, Region


class TiendaForm(forms.ModelForm):

    ciudad = forms.ModelChoiceField(
        queryset = Ciudad.objects.all(),
        empty_label="Seleccione ciudad"
    )

    region = forms.ModelChoiceField(
        queryset = Region.objects.all(),
        empty_label= "Seleccione región"
    )

    class Meta:
        model = Tienda
        fields = ('nombre', 'sucursal', 'direccion',
                  'ciudad', 'region', 'estado')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ProductoForm(forms.ModelForm):

    tienda = forms.ModelChoiceField(
        queryset = Tienda.objects.all(),
        empty_label = "Seleccione su tienda"
    )

    class Meta:
        model = Producto
        fields=('nombre','costo_presupuestado','costo_real','tienda','notas')



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class CompraForm(forms.ModelForm):

    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        empty_label = "Elija su producto"
    )

    class Meta:
        model = Compra
        fields = ('nombre','producto','comprado','usuario')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    
