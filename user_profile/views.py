from django.shortcuts import render
# Import UserProfile model
from .models import UserProfile

# Create your views here.

def user_profile(request):
    profile = UserProfile.objects.all().filter(user=request.user)
    return render(request, "user_profile/profile.html", {'profile':profile})