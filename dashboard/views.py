from django.shortcuts import render
from user_profile.models import UserCourse
from courses.models import ContentMedia, TestCourse
from status.models import Status
from django.db.models import Q

# Create your views here.

# Dashboard view
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
        # Obtengo el id del curso
        course_id = obj.course
    # Obtenemos el contenido del curso filtrando por el id del curso obtenido
    content_course = ContentMedia.objects.filter(content=course_id)
    # Obtenemos datos de examen filtrando por el id del curso
    content_test = TestCourse.objects.filter(content=course_id)
    if len(content_test) != 0:
        test_flag = course_id
    else:
        test_flag = 0
    return render(request, "dashboard/dashboard.html",{'usercourse': instancia, 'content_course': content_course, 'test':test_flag})

# Test view
def tests(request, pk):
    test = TestCourse.objects.filter(course=pk)
    return render(request, "dashboard/exams.html", {'test':test})