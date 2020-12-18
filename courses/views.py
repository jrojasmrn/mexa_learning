from django.shortcuts import render
#Import Courses model
from .models import Content
from django.db.models import Q

# Create your views here.

#Send Email Function
# def send_email():
#     from django.core.mail import send_mail
#     from mexaeducation import settings
#     subject = 'Solicitud de inscripción a curso'
#     message = 'El usuario %s con nombre de usuario %s y correo %s ha solicitado la inscripción al curso X' % ()
#     send_mail()

def courses(request):
    # Barra de búsqueda para los cursos
    queryset_title = request.GET.get("buscar")
    contents = Content.objects.all().filter(
        status = 1
    )
    if queryset_title:
        contents = Content.objects.filter(
            Q(title__icontains = queryset_title)
        )
    return render(request, "courses/courses.html", {'contents':contents})