from django.shortcuts import render, redirect
from user_profile.models import UserCourse
from courses.models import ContentMedia, TestCourse
from status.models import Status
from user_profile.models import ActivityUsers
from django.db.models import Q
#import forms
from .forms import UploadFile

# Create your views here.

# Dashboard view
def dashboard(request, pk, course_name, pk_media):
    # Cambiamos el status del curso filtrando el curso por el ID
    instancia = UserCourse.objects.filter(
        Q(id=pk),
        Q(status=1) | Q(status=3)
    )
    for obj in instancia:
        new_status = Status.objects.get(status='En proceso')
        obj.status = new_status
        obj.save()
        # Obtengo el id del curso
        course_id = obj.course
    # Obtenemos el contenido del curso filtrando por el id del curso obtenido
    content_course = ContentMedia.objects.filter(content=course_id)
    content_course_data = ContentMedia.objects.filter(content=course_id, id=pk_media)
    # Función para mandar las actividades de usuarios
    form = UploadFile()
    if request.method == "POST":
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('control-pane')
    # Datos que mandamos
    # user_logged = instancia.user
    # content_header
    # content_media
    return render(request, "dashboard/dashboard.html",{'form':form, 'usercourse': instancia, 'content_course': content_course, 'content_course_data':content_course_data})

# Test view
def tests(request, pk):
    test = TestCourse.objects.filter(course=pk)
    return render(request, "dashboard/exams.html", {'test':test})