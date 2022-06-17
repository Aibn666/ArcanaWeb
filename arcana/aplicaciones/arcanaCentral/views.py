from django.shortcuts import render

# Create your views here.

def arcanaHome(request):
    return render(request, 'arcana.html')

def index(request):
    return render(request, 'index.html')