from django.db import models
#Import Status Models
from status.models import Status

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imágen')
    video = models.URLField(verbose_name='Video', null=True, blank=True)
    multiimage = models.ImageField(verbose_name='Contenido multimedia', null=True, blank=True)
    multiimagetwo = models.ImageField(verbose_name='Contenido multimedia', null=True, blank=True)
    notes = models.TextField(verbose_name='Notas', default='No hay notas aún')
    advertisements = models.TextField(verbose_name='Anuncios', default='No hay anuncios aquí')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status', default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    #Cambiar nombre de modelo para mostrar
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-created']

    #Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return self.title