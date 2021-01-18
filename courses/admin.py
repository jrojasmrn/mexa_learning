from django.contrib import admin
#Import models
from .models import *

# Register your models here.

admin.site.register(ContentHeader)
admin.site.register(ContentMedia)
admin.site.register(TestCourse)
admin.site.register(SubscribeCourse)