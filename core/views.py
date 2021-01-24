from django.shortcuts import render
from user_profile.models import UserCourse, UserProfile
from .models import Advertisements, AssistanceUser
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

# assistance user function
def assistance_user(user):
    # Obtenemos la última hora de login del usuario
    last_login = User.objects.get(username=user).last_login
    # Validamos que el registro no exista para no duplicarlo
    validate_data = AssistanceUser.objects.values().filter(
        Q(assistance=last_login),
        Q(user=user)
    )
    if len(validate_data) == 0:
        # Insertamos el registro de la asistencia
        assistance_user_id = AssistanceUser.objects.create(
            assistance = last_login,
            user = user
        )
    # Si el registro existe, lo actualiza con la misma información
    else:
        assistance_user_id = AssistanceUser.objects.filter(
            Q(assistance=last_login),
            Q(user=user)
        ).update(
            assistance=last_login,
            user=user
        )

# create user profile function
def create_user_profile(user):
    # Validamos que el perfil no existe
    validate_data = UserProfile.objects.values().filter(
        Q(user=user)
    )
    if len(validate_data) == 0:
        # Creamos el registro en la tabla
        user_profile_id = UserProfile.objects.create(
            user=user
        )
    # Si el registro existe lo actualizamos con la misma información
    else:
        user_profile_id = UserProfile.objects.filter(
            Q(user=user)
        ).update(
            user=user
        )

# home principal view
def home(request):
    # Creamos registro de asistencia de la plataforma
    assistance_user(request.user)
    # Creamos el perfil del usuario si no existe
    create_user_profile(request.user)
    # Obtenemos los cursos del usuario
    usercourse = UserCourse.objects.all().filter(
        Q(user = request.user),
        Q(status = 1) | Q(status = 3) | Q(status = 4)
    )
    # Obtenemos los anuncios de usuario logeado
    adver = Advertisements.objects.all().filter(
        Q(user = request.user),
        Q(status = 1)
    )
    return render(request, "core/panel.html", {'usercourse': usercourse, 'adver':adver})

#User Ethics view
def ethics(request):
    return  render(request, "core/ethics.html")