from django.shortcuts import render
# Import UserProfile model
from .models import UserProfile
# Import Catalogue models
from catalogues.models import StatesList, LanguajeList

# Create your views here.

def user_profile(request):
    profile = UserProfile.objects.all().filter(user=request.user)
    return render(request, "user_profile/profile.html", {'profile':profile})

# Update user profile view
def update_user_profile(request):
    states = StatesList.objects.all()
    languajes = LanguajeList.objects.all()
    profile = UserProfile.objects.all().filter(user=request.user)
    return render(request, "user_profile/update_profile.html", {'profile':profile, 'states':states, 'languajes':languajes})