from django import forms

class ProveedoraForm(forms.Form):
    nom_proveedora = forms.CharField(label="Nombre empresa", max_length=100)
    nom_contacto = forms.CharField(label="Nombre contacto", max_length=50)
    correo = forms.EmailField(label="Correo contacto", max_length=100)
    tel = forms.IntegerField(label="Teléfono contacto")
    calle = forms.CharField(label="Calle (dirección)", max_length=100)
    numero = forms.IntegerField(label="Número (dirección)")
    complemento = forms.CharField(label="Complemento (dirección)", max_length=10, required=False)

class ItemForm(forms.Form):
    nom_item = forms.CharField(max_length=100)
    categoria = forms.CharField(max_length=30)
    unidad_cod_unidad = forms.IntegerField()
    cant_item = forms.IntegerField()
    costo_std = forms.IntegerField()

class ArticuloForm(forms.Form):
    nom_art = forms.CharField(max_length=100)
    item_cod_item = forms.IntegerField()
    proveedora_cod_proveedora = forms.IntegerField()

class EntradaForm(forms.Form):
    inventario_cod_art = forms.IntegerField()
    cantidad = forms.IntegerField()
    costo_unit = forms.IntegerField()
    descripcion = forms.CharField(max_length=100)

class SalidaForm(forms.Form):
    inventario_cod_art = forms.IntegerField()
    cantidad = forms.IntegerField()
    descripcion = forms.CharField(max_length=100)
