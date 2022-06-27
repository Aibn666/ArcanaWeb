from django.shortcuts import render
from .models import Ritual

# Create your views here.

def rituales(request):
    ritual = Ritual.objects.filter(estado = True)
    return render(request, 'rituales.html',{'rituales':ritual})