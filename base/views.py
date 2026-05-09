from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Certifique-se de que o template existe

def calculadora(request):
    return render(request, 'calculadora.html')