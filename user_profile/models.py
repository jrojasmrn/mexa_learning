from django.db import models
from django.contrib.auth.models import User
from courses.models import ContentHeader, ContentMedia
from status.models import StatusUserCourse, StatusSubscribeCourse, UserGradeStatus
from catalogues.models import StatesList, LanguajeList, UserGrades

# Create your models here.

class UserCourse(models.Model):
    user = models.ForeignKey(User, verbose_name='Nombre de usuario', on_delete=models.CASCADE)
    course = models.ForeignKey(ContentHeader, verbose_name='Nombre de curso', on_delete=models.CASCADE)
    status = models.ForeignKey(StatusUserCourse, verbose_name='Status', on_delete=models.CASCADE, default=1)
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

# User profile model
class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name='Nombre de usuario', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Descripción del usuario', null=True, blank=True)
    user_image = models.ImageField(verbose_name='Imágen de usuario', null=True, blank=True)
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

# Homework user files model
class ActivityUsers(models.Model):
    content = models.ForeignKey(ContentHeader, on_delete=models.CASCADE, verbose_name='Nombre de curso')
    content_media = models.ForeignKey(ContentMedia, on_delete=models.CASCADE, verbose_name='Nombre de contenido')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    act_file = models.FileField(verbose_name='Archivo')
    comment = models.TextField(verbose_name='Comentario')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')

    # Cambiar nombre para mostrar
    class Meta:
        verbose_name = "Actividad usuario"
        verbose_name_plural = "Actividades usuarios"

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return 'Actividad de %s - %s' % (self.user.get_full_name(), self.content)

# Homework's grade users
class ActivityGrades(models.Model):
    activity = models.ForeignKey(ActivityUsers, on_delete=models.CASCADE, verbose_name='Actividad')
    course = models.ForeignKey(ContentHeader, on_delete=models.CASCADE, verbose_name='Curso')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    grade = models.ForeignKey(UserGrades, on_delete=models.CASCADE, verbose_name='Calificacion', default='NA')
    comment = models.TextField(verbose_name='Comentario')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')

    # Cambiar nombre para mostrar
    class Meta:
        verbose_name = "Calificaciones de actividades"
        verbose_name_plural = "Calificaciones de actividades"

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return 'Calificacion de %s - %s' % (self.user, self.course)

# User course grade's model
class UserCourseGrade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    content = models.ForeignKey(ContentHeader, on_delete=models.CASCADE, verbose_name='Curso')
    calf = models.CharField(max_length=254, verbose_name='Calificacion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    status = models.ForeignKey(UserGradeStatus, on_delete=models.CASCADE, verbose_name='Status')

    # Cambiar nombre para mostrar
    class Meta:
        verbose_name = "Calificaciones de curso"
        verbose_name_plural = "Calificaciones de cursos"

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return 'Calificacion de %s - %s' % (self.user, self.content)

# User course certificate
class UserCertificates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    content = models.ForeignKey(ContentHeader, on_delete=models.CASCADE, verbose_name='Contenido')
    cert_file = models.CharField(max_length=254, verbose_name='Certificado')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')

    # Cambiar nombre para mostrar
    class Meta:
        verbose_name = "Certificado"
        verbose_name_plural = "Certificados"

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return 'Certificado de %s ' % (self.user)

# User general calf model
class UserGeneralGrades(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    calf = models.FloatField(verbose_name='Calificacion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    # Cambiar nombre para mostrar
    class Meta:
        verbose_name = "Promedio general"
        verbose_name_plural = "Promedios generales"

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return 'Promedio de %s ' % (self.user)