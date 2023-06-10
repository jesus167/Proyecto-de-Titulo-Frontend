from django import forms




class RegistroClientas(forms.Form):

    rut_clienta = forms.IntegerField()
    dv_clienta = forms.CharField(max_length=1)
    tipo_clienta = forms.IntegerField()
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    nom_fantasia = forms.CharField(max_length=100)
    rep_legal_cod_rep_legal = forms.IntegerField()
    correo = forms.EmailField(max_length=100)
    tel = forms.IntegerField()
    pais_cod_pais = forms.CharField()
    comuna_cod_comuna = forms.CharField()
    calle = forms.CharField(max_length=200)
    numero = forms.IntegerField()
    complemento = forms.CharField(max_length=10)
    giro = forms.CharField(max_length=200)

class RepresentanteLegal(forms.Form):
        rut_rep_legal= forms.IntegerField()
        dv_rep_legal= forms.CharField(max_length=1)
        nombre= forms.CharField(max_length=100)
        apellido= forms.CharField(max_length=100)
        correo= forms.EmailField(max_length=100)
        tel = forms.IntegerField()


class EditarClientas(forms.Form):
    tipo_clienta = forms.IntegerField()
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    nom_fantasia = forms.CharField(max_length=100)
    rep_legal_cod_rep_legal = forms.IntegerField()
    correo = forms.EmailField(max_length=100)
    tel = forms.IntegerField()
    pais_cod_pais = forms.CharField()
    comuna_cod_comuna = forms.CharField()
    calle = forms.CharField(max_length=200)
    numero = forms.IntegerField()
    complemento = forms.CharField(max_length=10)
    giro = forms.CharField(max_length=200)
