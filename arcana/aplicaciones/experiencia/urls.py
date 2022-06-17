from django.urls import path
from .views import preparativos, experiencia



urlpatterns = [
    path('', preparativos, name='preparativos'),
    path('experiencia/', experiencia, name='experiencia'),
]