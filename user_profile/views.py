from django.shortcuts import render, redirect
# Import models
from .models import UserProfile, UserCourse
from courses.models import SubscribeCourse
# Import Forms
from .forms import UpdateProfile

# Create your views here.

# User profile view
def user_profile(request):
    profile = UserProfile.objects.all().filter(user=request.user)
    content = UserCourse.objects.all().filter(user=request.user)
    usersubs = SubscribeCourse.objects.all().filter(user=request.user, status=5)
    return render(request, "user_profile/profile.html", {'profile': profile, 'content': content, 'usersubs': usersubs})

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