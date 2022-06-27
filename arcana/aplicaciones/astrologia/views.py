from django.shortcuts import render
from .models import Post

# Create your views here.
def post (request):
    return render(request, 'post.html')
    
def astrologia(request):
    posts = Post.objects.filter(estado = True)
    return render(request,'astrologia.html',{'posts':posts})
