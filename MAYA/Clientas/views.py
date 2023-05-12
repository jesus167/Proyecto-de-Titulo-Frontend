from django.shortcuts import render



def clientas(request):
    return render (request, 'Clientas/clientas.html')

def registro_clientas(request):
    return render (request, 'Clientas/registro_clientas.html')

def listar_clientas(request):
    return render (request, 'Clientas/listar_clientas.html')

