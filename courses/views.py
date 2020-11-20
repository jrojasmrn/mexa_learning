from django.shortcuts import render
#Import Courses model
from .models import Content

# Create your views here.

def courses(request):
    contents = Content.objects.all()
    return render(request, "courses/courses.html", {'contents':contents})