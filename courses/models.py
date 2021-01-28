from django.db import models
# Import Status Models
from status.models import Status, StatusSubscribeCourse
# Import catalogues
from django.contrib.auth.models import User
# Create your models here.

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

# Content courses model
class ContentMedia(models.Model):
    name = models.CharField(max_length=254, verbose_name='Nombre de contenido')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True, default='No hay descripción')
    notes = models.TextField(verbose_name='Notas', null=True, blank=True, default='No hay notas')
    g_suite = models.CharField(max_length=254, verbose_name='Documentos Google', null=True, blank=True)
    g_suite_slides = models.CharField(max_length=254, verbose_name='Documentos Google', null=True, blank=True)
    g_suite_sheets = models.CharField(max_length=254, verbose_name='Documentos Google', null=True, blank=True)
    video = models.URLField(verbose_name='Video', null=True, blank=True)
    genially = models.URLField(verbose_name='Link de Genially', null=True, blank=True)
    pdf = models.FileField(verbose_name='Seleccione documento PDF', null=True, blank=True)
    images = models.ImageField(verbose_name='Seleccione imágen', null=True, blank=True)
    activity_name = models.CharField(max_length=254, verbose_name='Nombre de actividad', null=True, blank=True)
    activity_description = models.TextField(verbose_name='Descripcion de actividad', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado')
    content = models.ForeignKey(ContentHeader, on_delete=models.CASCADE, verbose_name='Nombre de curso')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status', default=1)

    # Cambiar nombre de modelo para mostrar
    class Meta:
        verbose_name = "Contenido de curso"
        verbose_name_plural = "Contenido de cursos"
        ordering = ['content']

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return "Contenido %s de curso %s" % (self.name, self.content)

# Test courses model
class TestCourse(models.Model):
    content = models.ForeignKey(ContentHeader, on_delete=models.CASCADE, verbose_name='Nombre de curso')
    question = models.CharField(max_length=254, verbose_name='Pregunta')
    answer_v = models.CharField(max_length=254, verbose_name='Respuesta correcta')
    answer_f1 = models.CharField(max_length=254, verbose_name='Respuesta incorrecta')
    answer_f2 = models.CharField(max_length=254, verbose_name='Respuesta incorrecta')
    answer_f3 = models.CharField(max_length=254, verbose_name='Respuesta incorrecta')

    # Cambiar nombre de modelo para mostrar
    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Examenes"
        ordering = ['content']

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return "Pregunta %s" % (self.question)

# Subscribe course model
class SubscribeCourse(models.Model):
    course = models.ForeignKey(ContentHeader, on_delete=models.CASCADE, verbose_name='Curso')
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Usuario')
    subscribe_time = models.DateTimeField(auto_now_add=True, verbose_name='Solicitado')
    status = models.ForeignKey(StatusSubscribeCourse, on_delete=models.CASCADE, verbose_name='Status')

    # Cambiar nomobre de modelo para mostrar
    class Meta:
        verbose_name = "Suscripción"
        verbose_name_plural = "Suscripciones"
        ordering = ['-subscribe_time']

    # Definición de nombre para identificar el registro
    def __str__(self):
        return 'Solicitud de %s al curso %s' % (self.user, self.course)
