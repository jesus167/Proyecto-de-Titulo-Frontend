from django import forms

class PedidoForm(forms.Form):
    fecha_compromiso = forms.DateField()
    clienta_cod_clienta = forms.IntegerField()


class DetallePedidoForm(forms.Form):
    pedido_cod_pedido = forms.IntegerField()
    categoria = forms.IntegerField()
    item_cod_item = forms.IntegerField(required=False)
    ft_cod_ft = forms.IntegerField(required=False)
    cantidad = forms.IntegerField()