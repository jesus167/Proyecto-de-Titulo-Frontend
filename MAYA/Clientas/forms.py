from django import forms
from .models import *



class RegistroClientas(forms.ModelForm):
    
    class Meta:
        model = Clienta
        fields = '__all__'
        # fields = ['Rut', 'DV', 'Tipo Clienta', 'Nombre', 'Apellido', 'Nombre Fantasia', 'Representante legal', 'Correo', 'Teléfono',
        #           'Calle', 'Número', 'Complemento', 'Comuna', 'Pais', 'Giro']