from django.urls import path
from .views import rituales, ritual

urlpatterns = [
    path('', rituales, name='rituales'),
    path('ritual/',ritual, name='ritual'),
]