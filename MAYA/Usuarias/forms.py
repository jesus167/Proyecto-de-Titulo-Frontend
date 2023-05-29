from django import forms


class RegistrarUsuariaForm(forms.Form):
    
    correo = forms.EmailField()
    pwd = forms.CharField(widget=forms.PasswordInput)
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    perfil_cod_perfil = forms.ChoiceField(choices=[(1, 'Administradora'), (2, 'Encargada de cocina'), (3, 'Asistenta de cocina'), (4, 'Encargada de logística')])
