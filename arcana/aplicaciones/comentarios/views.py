from django.shortcuts import render

# Create your views here.

def contactar(request):
    return render(request, 'contacto.html')

def verComentarios(request):
    return render(request, 'Comentarios.html')