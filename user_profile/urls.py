from django.urls import path
#Importing views file
from . import views

urlpatterns = [
    path('user-profile', views.user_profile, name="user-profile"),
    path('update-user-profile/<int:pk>', views.update_user_profile, name="update-user-profile")
]