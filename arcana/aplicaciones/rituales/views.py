from django.shortcuts import render

# Create your views here.

def rituales(request):
    return render(request, 'rituales.html')

def ritual(request):
    return render(request, 'ritual.html')