from django.shortcuts import render, redirect
# Import UserProfile model
from .models import UserProfile
# Import Catalogue models
from catalogues.models import StatesList, LanguajeList
# Import Forms
from .forms import UpdateProfile

# Create your views here.

def user_profile(request):
    profile = UserProfile.objects.all().filter(user=request.user)
    return render(request, "user_profile/profile.html", {'profile':profile})

# Update user profile view
def update_user_profile(request):
    profile = UserProfile.objects.all().filter(user=request.user)
    states = StatesList.objects.all()
    languajes = LanguajeList.objects.all()

    # Recuperamos el ID del perfil
    instance = profile['id']
    # Comprobamos que se está mandando un POST
    if request.method == "POST":
        # Añadimos los datos recibidos del formulario
        form = UpdateProfile(request.POST, profile['id'])
        # Confirmamos si el formulario es válido
        if form.is_valid():
            # Actualizamos la instancia
            form = form.save(commit=False)
            form.save()
            # Cuando se ingrese la información redireccionamos al perfil
            return redirect('user-profile')
        # Si no es válido, no le pasamos información
    else:
        form = UpdateProfile()
    return render(request, "user_profile/update_profile.html", {'form':form, 'profile':profile, 'states':states, 'languajes':languajes})