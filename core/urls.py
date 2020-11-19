from django.urls import path
#Importing views file
from . import views

urlpatterns = [
    path('', views.home, name="control-pane"),
]