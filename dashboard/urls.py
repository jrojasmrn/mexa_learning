from django.urls import path
#Importing views file
from . import views

urlpatterns = [
    path('<str:pk>/<str:course_name>', views.dashboard, name='dashboard')
]