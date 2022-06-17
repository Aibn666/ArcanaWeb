from django.shortcuts import render
from .models import Post

# Create your views here.

def astrologia(request):
    posts = Post.objects.filter(estado = True)
    return render(request,'astrologia.html',{'posts':posts})

def index(request):
    return render(request, 'index.html')