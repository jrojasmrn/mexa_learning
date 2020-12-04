from django.db import models
from django.contrib.auth.models import User
from courses.models import Content
from status.models import Status
from catalogues.models import StatesList, LanguajeList

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

# User Certificates model
class UserCertificates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    course = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='Curso')
    certificate = models.FileField(verbose_name='Certificado')
    certificate_date = models.DateTimeField(verbose_name='Fecha de certificación')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status')

# User profile model
class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name='Nombre de usuario', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Descripción del usuario', null=True, blank=True)
    user_image = models.ImageField(verbose_name='Imágen de usuario', null=True, blank=True)
    certificates = models.ForeignKey(UserCertificates, on_delete=models.CASCADE, verbose_name='Certificados', null=True, blank=True)
    location = models.ForeignKey(StatesList, verbose_name='Estado', on_delete=models.CASCADE, null=True, blank=True)
    languaje = models.ForeignKey(LanguajeList, verbose_name='Lenguaje', on_delete=models.CASCADE, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    # Cambiar nombre para mostrar
    class Meta:
        verbose_name = "Perfil de usuario"
        verbose_name_plural = "Perfiles de usuarios"

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return 'Perfil de %s' % (self.user.get_full_name())