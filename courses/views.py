from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import datetime
# Import Contents model
from .models import Content, SubscribeCourse

# Create your views here.

# Suscribe course function
def subs_course(content, user):
    subscribe_course_id = SubscribeCourse.objects.create(
        subscribe_time=datetime.now(),
        course_id=content,
        status_id=5, # Viene por default, ya que es el ID - En espera
        user_id=user
    )

# Showing all courses function
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

#Preview view Content
def preview_content(request, pk):
    preview = Content.objects.filter(id=pk)
    # Si el usuario solicita acceso a un curso, insertamos el registro en la tabla de solicitud de inscripción
    if request.method == 'POST':
        for i in preview:
            content = preview[0]
        user = request.user.id
        subs_course(content, user)
        return redirect('control-pane')
    return render(request, "courses/preview_course.html",{'preview':preview})