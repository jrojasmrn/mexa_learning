from django.urls import path
#Importing views file
from . import views

urlpatterns = [
    path('forum/', views.forum, name='forum'),
]