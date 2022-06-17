
from operator import index
from django.urls import path
from .views import astrologia, index



urlpatterns = [
    path('', astrologia, name='astrologia'),
    path('index/', index, name='index'),
]