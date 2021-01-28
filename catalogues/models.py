from django.db import models

# Create your models here.

# States list catalogue
class StatesList(models.Model):
    state_name = models.CharField(max_length=254, verbose_name='Nombre de estado')

    # Cambiar nombre para mostrar
    class Meta:
        verbose_name = "Estados"
        verbose_name_plural = "Estados"

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return '%s' % (self.state_name)

# Languaje list catalogue
class LanguajeList(models.Model):
    languaje_name = models.CharField(max_length=254, verbose_name='Lenguaje')

    # Cambiar nombre para mostrar
    class Meta:
        verbose_name = "Lenguaje"
        verbose_name_plural = "Lenguajes"

    # Cambio de nombre de proyectos para mostrar
    def __str__(self):
        return '%s' % (self.languaje_name)

# User Grades model
class UserGrades(models.Model):
    grade = models.CharField(max_length=254, verbose_name='Calificacion')

    # Cambiar nombre para mostrar
    class Meta:
        verbose_name = "Calificacion"
        verbose_name_plural = "Calificaciones"

    # Cambio de nombre para mostrar información
    def __str__(self):
        return self.grade