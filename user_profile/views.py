from django.shortcuts import render, redirect
# Import UserProfile model
from .models import UserProfile
# Import Catalogue models
from catalogues.models import StatesList, LanguajeList
# Import Forms
from .forms import UpdateProfile

# Create your views here.

# User profile view
def user_profile(request):
    # import pdb
    # pdb.set_trace()
    profile = UserProfile.objects.all().filter(user=request.user)
    return render(request, "user_profile/profile.html", {'profile':profile})

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