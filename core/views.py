from django.shortcuts import render
from user_profile.models import UserCourse
from django.db.models import Q

# Create your views here.

def home(request):
    usercourse = UserCourse.objects.all().filter(
        Q(user = request.user),
        Q(status = 1) | Q(status = 3) | Q(status = 4)
    )
    return render(request, "core/panel.html", {'usercourse': usercourse})
