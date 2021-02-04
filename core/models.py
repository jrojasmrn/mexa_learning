from django.db import models
from django.contrib.auth.models import User
from status.models import Status

# Create your models here.

# advertisements model

# Advertisements model
class Advertisements(models.Model):
    title = models.CharField(max_length=254, verbose_name='Titulo')
    content = models.TextField(verbose_name='Anuncio')
    image_adver = models.ImageField(verbose_name='Imagen de anuncio', null=True, blank=True)
    link_adver = models.URLField(verbose_name='Links', null=True, blank=True)
    user = models.ManyToManyField(User, verbose_name='Usuarios', null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status', default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    # Cambiar nombre para mostrar
    class Meta:
        verbose_name = "Anuncio"
        verbose_name_plural = "Anuncios"

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return 'Anuncio %s' % (self.title)

# Assistance user model
class AssistanceUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    assistance = models.DateTimeField(verbose_name='Asistencia')

    # Cambiar nombre para mostrar
    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return '%s - %s' % (self.user, self.assistance)