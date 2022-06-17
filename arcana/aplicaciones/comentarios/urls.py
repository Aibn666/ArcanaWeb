from django.urls import path
from .views import contactar, verComentarios



urlpatterns = [
    path('', contactar, name='contactar'),
    path('verComentarios/', verComentarios, name='verComentarios'),
]