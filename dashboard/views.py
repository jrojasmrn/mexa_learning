from django.shortcuts import render
from user_profile.models import UserCourse
from status.models import Status
from django.db.models import Q

# Create your views here.

def dashboard(request):
    # Obtenemos nuestro ID
    id_course = int(request.GET['usercourse'])
    usercourse = UserCourse.objects.filter(
        Q(id = id_course),
        Q(status = 1) | Q(status = 3)
    )
    for obj in usercourse:
        new_status = Status.objects.get(status='En proceso')
        obj.status = new_status
        obj.save()
    return render(request, "dashboard/dashboard.html", {'usercourse':usercourse})