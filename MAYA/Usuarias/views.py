from django.shortcuts import render

# Create your views here.

def usuarias(request):
    return render(request, 'Usuarias/usuarias.html')