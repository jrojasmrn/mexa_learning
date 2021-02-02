from django.urls import path
#Importing views file
from . import views

urlpatterns = [
    path('<int:pk>/<str:course_name>/<int:pk_media>', views.dashboard, name='dashboard'),
    path('test/<int:pk>', views.tests, name='test_course'),
    path('test/results/<int:pk>', views.user_results, name='user_results'),
    # URL PRD Certificate
    path('certificate/', views.create_certificate, name='certificate')
]