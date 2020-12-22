from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import datetime
# Import Contents model
from .models import Content, SubscribeCourse
from user_profile.models import UserCourse

# Create your views here.

# Showing all courses view
def courses(request):
    # Obtenemos todos los cursos con status 1 - activos
    queryset_title = request.GET.get("buscar")
    contents = Content.objects.all().filter(
        status = 1
    )
    # Una vez tenemos los cursos activos, hacemos un filtrado por nombre en los cursos
    if queryset_title:
        contents = Content.objects.filter(
            Q(title__icontains = queryset_title)
        )
    return render(request, "courses/courses.html", {'contents':contents})

# Suscribe course function
def subs_course(content, user):
    subscribe_course_id = SubscribeCourse.objects.create(
        subscribe_time=datetime.now(),
        course_id=content,
        status_id=5, # Viene por default, ya que es el ID - En espera
        user_id=user
    )

def validate_user_curses(pk):
    id_usercourse = UserCourse.objects.filter(course=pk)
    id_subs = SubscribeCourse.objects.filter(course=pk)
    if id_usercourse:
        validator = 1
    elif id_subs:
        validator = 2
    else:
        validator = 0
    return validator

#Preview content view
def preview_content(request, pk):
    preview = Content.objects.filter(id=pk)
    # Determinar si el usuario ya hizo solicitud o ya lo tiene agregado
    usercourse_data = validate_user_curses(pk)
    # Si el usuario solicita acceso a un curso, insertamos el registro en la tabla de solicitud de inscripción
    if request.method == 'POST':
        # Obtenemos el ID del curso y el ID de usuario
        content = pk
        user = request.user.id
        # función para insertar la solicitud
        subs_course(content, user)
        # Redireccionamos al perfil
        return redirect('user-profile')
    return render(request, "courses/preview_course.html",{'preview':preview, 'usercourse_data':usercourse_data})