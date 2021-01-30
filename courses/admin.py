from django.contrib import admin
#Import models
from .models import *

# Register your models here.

admin.site.register(ContentHeader)
admin.site.register(ContentMedia)
admin.site.register(QuestionsTest)
admin.site.register(AnswersTest)
admin.site.register(AnsUserTest)
admin.site.register(SubscribeCourse)