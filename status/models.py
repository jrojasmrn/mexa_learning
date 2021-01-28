from django.db import models

# Create your models here.

class Status(models.Model):
    status = models.CharField(max_length=50, verbose_name='Status')

    class Meta:
        verbose_name='Status'
        verbose_name_plural='Status'

    def __str__(self):
        return self.status

# UserCourse Status
class StatusUserCourse(models.Model):
    status = models.CharField(max_length=50, verbose_name='Status')

    class Meta:
        verbose_name = 'User course Status'
        verbose_name_plural = 'User course Status'

    def __str__(self):
        return self.status

# SubscribeCourse Status
class StatusSubscribeCourse(models.Model):
    status = models.CharField(max_length=50, verbose_name='Status')

    class Meta:
        verbose_name = 'Subscribe course Status'
        verbose_name_plural = 'Subscribe course Status'

    def __str__(self):
        return self.status