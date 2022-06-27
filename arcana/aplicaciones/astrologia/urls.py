
from django.urls import path
from .views import astrologia, post



urlpatterns = [
    path('', astrologia, name='astrologia'),
    path('post/', post, name='post'),
]