from django.contrib import admin
#Import models
from .models import *

# Register your models here.

admin.site.register(Content)

admin.site.register(SubscribeCourse)

admin.site.register(ContentHeader)
admin.site.register(ModulesCourses)
admin.site.register(ContentCourseMedia)