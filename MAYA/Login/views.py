from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import  CustomUserCreationForm


# Create your views here.

# def login(request):
#     message = None
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     message = "te has identificado de modo correcto"
#                     print("se ha logeado")
#                 else:
#                     message = "tu usuario está inactivo"
#                     print("algo salio mal")
#             else:
#                 message = "nombre de usuario o contraseña incorrecto"
#                 print("algo salio mal")
#     else:
#         form = LoginForm()
#         print("algo salio mal")
#     return render(request, 'Login/login.html', {'message':message, 'form':form})

def login(request):
    return render(request, 'Login/login.html')


def registro(request):
    return render(request, 'Login/registro.html')
def registro (request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'Login/registro.html', data)