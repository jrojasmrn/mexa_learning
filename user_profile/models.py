from django.db import models
from django.contrib.auth.models import User
from courses.models import Content
from status.models import Status

# Create your models here.

class UserCourse(models.Model):
    user = models.ForeignKey(User, verbose_name='Nombre de usuario', on_delete=models.CASCADE)
    course = models.ForeignKey(Content, verbose_name='Nombre de curso', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, verbose_name='Status', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    # Cambiar nombre de modelo para mostrar
    class Meta:
        verbose_name = "Curso de usuario"
        verbose_name_plural = "Cursos de usuarios"
        ordering = ['-created']

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return 'Curso de %s - %s %s' % (self.course, self.user.first_name, self.user.last_name)