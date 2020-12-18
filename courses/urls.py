from django.urls import path
#Importing views file
from . import views

urlpatterns = [
    path('all', views.courses, name='courses'),
    path('preview-course/<int:pk>', views.preview_content, name='preview-course')
]