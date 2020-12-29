from django.db import models
# Import Status Models
from status.models import Status
# Import catalogues
from catalogues.models import ContentType
from django.contrib.auth.models import User
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

# Subscribe course model
class SubscribeCourse(models.Model):
    course = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='Curso')
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Usuario')
    subscribe_time = models.DateTimeField(auto_now_add=True, verbose_name='Solicitado')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status')

    # Cambiar nomobre de modelo para mostrar
    class Meta:
        verbose_name = "Suscripción"
        verbose_name_plural = "Suscripciones"
        ordering = ['-subscribe_time']

    # Definición de nombre para identificar el registro
    def __str__(self):
        return 'Solicitud de %s al curso %s' % (self.user, self.course)

# Cambios de rama 'cursos'

# Content model
class ContentHeader(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imágen')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status', default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    # Cambiar nombre de modelo para mostrar
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-created']

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return self.title

# Modules content model
class ModulesCourses(models.Model):
    content = models.ForeignKey(ContentHeader, on_delete=models.CASCADE, verbose_name='Contenido')
    module_name = models.CharField(max_length=254, verbose_name='Nombre de modulo')

    # Cambiar nombre de modelo para mostrar
    class Meta:
        verbose_name = "Modulo"
        verbose_name_plural = "Modulos"
        ordering = ['content']

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return self.module_name

# Content courses model
class ContentCourseMedia(models.Model):
    content = models.ForeignKey(ContentHeader, on_delete=models.CASCADE, verbose_name='Nombre de curso')
    module = models.ForeignKey(ModulesCourses, on_delete=models.CASCADE, verbose_name='Nombre de módulo')
    name = models.CharField(max_length=254, verbose_name='Nombre de contenido')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    notes = models.TextField(verbose_name='Notas', default='No hay notas aún')
    notices = models.TextField(verbose_name='Anuncios', default='No hay anuncios aquí')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='Tipo de contenido')
    g_suite = models.CharField(max_length=254, verbose_name='Documentos Google', null=True, blank=True)
    video = models.URLField(verbose_name='Video', null=True, blank=True)
    pdf = models.FileField(verbose_name='Seleccione documento PDF', null=True, blank=True)
    images = models.ImageField(verbose_name='Seleccione imágen', null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status', default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    # Cambiar nombre de modelo para mostrar
    class Meta:
        verbose_name = "Contenido de curso"
        verbose_name_plural = "Contenido de cursos"
        ordering = ['content']

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return "Contenido %s de módulo %s - %s" % (self.name, self.module, self.content)