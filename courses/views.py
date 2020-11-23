from django.shortcuts import render
#Import Courses model
from .models import Content
from django.db.models import Q

# Create your views here.

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