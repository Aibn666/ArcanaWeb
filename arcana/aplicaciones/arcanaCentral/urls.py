
from django.urls import path
from .views import arcanaHome, index



urlpatterns = [
    path('arcana/', arcanaHome, name='arcanaHome'),
    path('', index, name='index'),
]