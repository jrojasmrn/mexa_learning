from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserCourse)
admin.site.register(UserProfile)
admin.site.register(ActivityUsers)
admin.site.register(ActivityGrades)