from django.db import models
# Import Status model
from status.models import Status
# Import Content_media model
from courses.models import ContentMedia, ContentHeader
# Import User model
from django.contrib.auth.models import User

# Create your models here.

# Chech_media model
class CheckMediaUser(models.Model):
    content_media = models.ForeignKey(ContentMedia, on_delete=models.CASCADE, verbose_name='Contenido')
    course = models.ForeignKey(ContentHeader, on_delete=models.CASCADE, verbose_name='Curso')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status')

    # Cambiar nombre de modelo para mostrar
    class Meta:
        verbose_name = "Check de modulo"
        verbose_name_plural = "Check de modulos"

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return '%s - %s' % (self.user, self.content_media)