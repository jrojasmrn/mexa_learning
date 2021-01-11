from django.shortcuts import render
from user_profile.models import UserCourse
from courses.models import ContentCourseMedia, ModulesCourses
from status.models import Status
from django.db.models import Q

# Create your views here.

def dashboard(request, pk, course_name):
    # Cambiamos el status del curso filtrando el curso por el ID
    instancia = UserCourse.objects.filter(
        Q(id=pk),
        Q(status=1) | Q(status=3)
    )
    for obj in instancia:
        new_status = Status.objects.get(status='En proceso')
        obj.status = new_status
        obj.save()
        course_id = obj.course
    # # Obtenemos los módulos totales del curso
    # modules = ModulesCourses.objects.filter(content=course_id)
    # # Obtenemos el contenido de cada modulo
    # content = ContentCourseMedia.objects.filter(content=course_id)
    content_module = ContentCourseMedia.objects.filter(content=course_id)
    return render(request, "dashboard/dashboard.html", {'usercourse':instancia, 'content':content_module})