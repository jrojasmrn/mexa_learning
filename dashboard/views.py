from django.shortcuts import render, redirect
from user_profile.models import UserCourse
from courses.models import ContentMedia, TestCourse
from status.models import Status, StatusUserCourse
# Import . models
from .models import CheckMediaUser
from django.db.models import Q
#import forms
from .forms import UploadFile

# Create your views here.

# Checking module of course
def check_module_user(user, course, content_media):
    status = Status.objects.get(id=1)
    # Actualizamos el status del registro
    check_module_user_id = CheckMediaUser.objects.filter(
        Q(course=course),
        Q(content_media=content_media),
        Q(user=user)
    ).update(
        status=status
    )

# register course information to check function
def register_course(user, course):
    status = Status.objects.get(id=2)
    # Obtenemos el contenido media de los cursos
    media = ContentMedia.objects.filter(
        Q(content=course),
        Q(status=1)
    )
    # Iteramos en el contenido media
    for data in media:
        # Validamos que el registro no existe
        validate_data = CheckMediaUser.objects.values().filter(
            Q(course=course),
            Q(user=user),
            Q(content_media=data)
        )
        # Si no existe el registro, lo creamos
        if len(validate_data) == 0:
            check_media_id = CheckMediaUser.objects.create(
                content_media= data,
                course=course,
                user=user,
                status=status
            )
        # Si existe, lo actualizamos con la misma información
        else:
            check_media_user_id = CheckMediaUser.objects.filter(
                Q(course=course),
                Q(user=user),
                Q(content_media=data)
            ).update(
                content_media=data,
                course=course,
                user=user
            )

# Dashboard view
def dashboard(request, pk, course_name, pk_media):
    # Cambiamos el status del curso filtrando el curso por el ID
    instancia = UserCourse.objects.filter(
        Q(id=pk),
        Q(status=1) | Q(status=3)
    )
    for obj in instancia:
        new_status = StatusUserCourse.objects.get(status='En proceso')
        obj.status = new_status
        obj.save()
        # Obtengo el id del curso
        course_id = obj.course
    # Llenamos la tabla para hacer el check
    register_course(request.user, course_id)
    # Obtenemos el nombre de los cursos para mostrar
    content_course = CheckMediaUser.objects.filter(
        Q(course=course_id),
        Q(user=request.user)
    )
    # Actualizamos status de la clase
    check_module_user(request.user, course_id, pk_media)
    # Obtenemos el contenido del curso filtrando por el id del curso obtenido
    content_course_data = ContentMedia.objects.filter(content=course_id, id=pk_media)
    # Función para mandar las actividades de usuarios
    form = UploadFile()
    if request.method == 'POST':
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('control-pane')
    return render(request, "dashboard/dashboard.html",{'form':form, 'usercourse': instancia, 'content_course': content_course, 'content_course_data':content_course_data})

# Test view
def tests(request, pk):
    test = TestCourse.objects.filter(content=pk)
    return render(request, "dashboard/exams.html", {'test': test})