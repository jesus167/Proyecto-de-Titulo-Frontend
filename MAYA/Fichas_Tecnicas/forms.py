from django import forms



class FtForm(forms.Form):
    nom_ft = forms.CharField(label="Nombre ficha técnica (ej.: Puré de papas)", max_length=100)
    rendimiento = forms.IntegerField(label="Rendimiento")
    observacion = forms.CharField(label="Observación", max_length=500, required=False, widget=forms.Textarea(attrs={'rows': 3}))
    img_ft = forms.ImageField(label="Imagen ficha técnica", required=False)


class DetalleIngredienteForm(forms.Form):
    ft_cod_ft = forms.IntegerField()
    item_cod_item = forms.IntegerField()   
    cantidad = forms.IntegerField()


class DetallePreparacionForm(forms.Form):
    ft_cod_ft = forms.IntegerField()
    instruccion = forms.CharField(max_length=300)