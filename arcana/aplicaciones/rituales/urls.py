from django.urls import path
from .views import rituales

urlpatterns = [
    path('', rituales, name='rituales'),
]