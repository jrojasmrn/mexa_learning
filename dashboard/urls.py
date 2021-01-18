from django.urls import path
#Importing views file
from . import views

urlpatterns = [
    path('<int:pk>/<str:course_name>', views.dashboard, name='dashboard'),
    path('test/<int:pk>', views.tests, name='test_course'),
]