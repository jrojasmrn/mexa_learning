from django.shortcuts import render, redirect
from django.db.models import Q
# Import models
from .models import *
from courses.models import SubscribeCourse
# Import Forms
from .forms import UpdateProfile

# Create your views here.

# User profile view
def user_profile(request):
    # Obtengo los datos del perfil del usuario
    profile = UserProfile.objects.all().filter(user=request.user)
    # Obtengo los cursos del usuario
    content = UserCourse.objects.all().filter(
        Q(user=request.user),
        Q(status=1) | Q(status=3) | Q(status=4)
    )
    # Obtengo las solicites a cursos del usuario
    usersubs = SubscribeCourse.objects.all().filter(user=request.user, status=1)
    # Obtengo las acts del usuario
    act = ActivityUsers.objects.filter(
        Q(user=request.user)
    )
    # Obtendo las calfs del usuario
    calfs = ActivityGrades.objects.filter(
        Q(user=request.user)
    )
    return render(request, "user_profile/profile.html", {'profile': profile, 'content': content, 'usersubs': usersubs, 'act': act, 'calfs': calfs})

# Update user profile view
def update_user_profile(request, pk):
    instancia = UserProfile.objects.get(id=pk)
    form = UpdateProfile(instance=instancia)
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            instancia.user_image = form.cleaned_data['user_image']
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('user-profile')
    profile = UserProfile.objects.all().filter(user=request.user)
    return render(request, "user_profile/update_profile.html", {'form':form, 'profile':profile})