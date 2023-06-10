import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm


url_login = "http://127.0.0.1:8000/api/login/"


# Create your views here.



def inicio_sesion(request):
    

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            canal = 1
            usuario = {
                        'correo': username,
                        'pwd': password,
                        'canal': canal
                    }
            print(usuario)
            data = requests.post(url_login, json = usuario)
            print(data.status_code)
            if data.status_code == 200:
                return redirect('Home')
            else:
                return redirect('Login')
        else:
            print(data.status_code)
            print('no logueado')
            return render(request, 'Login/login.html')

    return render(request, 'Login/login.html')

