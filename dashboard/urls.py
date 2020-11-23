from django.urls import path
#Importing views file
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard')
]