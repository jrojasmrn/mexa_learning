from django.urls import path
#Importing views file
from . import views

urlpatterns = [
    path('', views.admin_panel, name='admin-panel'),
    # URLS for users
    path('users/', views.users_panel, name='users'),
    path('create_user/', views.create_user, name='create_user'),
    path('update_user/<int:id_user>/', views.update_user, name='update_user'),
    # URLS for content
    path('admin-courses/', views.courses_header, name='admin-courses'),
    path('create_course/', views.create_content, name='create_content'),
    path('update_course/<int:id_course>/', views.update_content, name='update_course'),
    # URLS for content media
    path('content_media/<int:id_course>/', views.content_media, name='admin-content_media'),
    path('create_media/<int:id_course>/', views.create_media, name='create_media'),
    path('update_media/<int:id_media>/', views.update_content_media, name='update_media'),
    # URLS for user subs
    path('user_subs/', views.subs_control, name='user_subs'),
    path('assign_course/', views.create_user_course, name='assign_course'),
    path('update_assign_course/<int:pk>/', views.update_user_course, name='update_assign_course'),
    # URLS for notices
    path('notices/', views.notices_users, name='notices_user'),
    path('create_notice/', views.create_notice, name='create_notice'),
    path('update_notice/<int:id_notice>', views.update_notice, name='update_notice'),
    # URLS for assistment user
    path('assistment_user/<int:id_user>', views.assistment_user, name='assistment_user'),
    path('grades/<int:user>/<int:course>/<int:act>', views.activity_grade, name='activity_grade'),
]