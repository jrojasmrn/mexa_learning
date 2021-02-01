from django.contrib import admin
#Import models
from .models import *

# Register your models here.

admin.site.register(Status)
admin.site.register(StatusUserCourse)
admin.site.register(StatusSubscribeCourse)
admin.site.register(UserGradeStatus)