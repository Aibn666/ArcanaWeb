from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Ritual(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título', max_length = 90, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    descripcion = models.CharField('Descripción', max_length = 110, blank = False, null = False)
    imagen = models.URLField(max_length = 255, blank = False, null= False)
    contenido = RichTextField()
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Ritual'
        verbose_name_plural = 'Rituales'

    def __str__(self):
        return self.titulo