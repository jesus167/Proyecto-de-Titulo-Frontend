from django import forms

class PwdRestore(forms.Form):
    correo = forms.CharField()
    new_pass = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())

class CierreSesion(forms.Form):
    correo = forms.CharField()
    canal = 1
    