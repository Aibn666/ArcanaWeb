from django.shortcuts import render

# Create your views here.

def preparativos (request):
    return render (request, 'preparativos.html')

def experiencia(request):
    return render (request, 'experiencia.html')