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
    # Obtenemos la calificacion del curso final
    course_calf = UserCourseGrade.objects.filter(
        Q(user=request.user)
    )
    # Obtenemos los certificados del usuario
    user_certs = UserCertificates.objects.filter(
        Q(user=request.user)
    )
    #
    # Calculamos el promedio general del usuario
    # Obtenemos la calificacion de todos los cursos que tenga
    final_calf_course = 0
    final_calf_act = 0
    user_course_grades = UserCourseGrade.objects.filter(
        Q(user=request.user)
    )
    # Si existe el registro
    if user_course_grades:
        # Iteramos en el queryset
        for data_grade in user_course_grades:
            # Sumamos todas las calfs de cursos del usuario
            final_calf_course += float(data_grade.calf)
        cant_courses = len(user_course_grades)
        # Obtenemos las calificaciones de las actividades
        user_act_grades = ActivityGrades.objects.filter(
            Q(user=request.user)
        )
        for data_acts in user_act_grades:
            # Sumamos todas las calfs de actividades del usuario
            final_calf_act += float(data_acts.grade.grade)
        cant_acts = len(user_act_grades)
        final_cant = cant_acts+cant_courses
        final_prom_user = (final_calf_act+final_calf_course)/final_cant
        if final_prom_user < 7:
            final_prom_user = 5
        # Validamos que el registro no exista
        validate_data = UserGeneralGrades.objects.values().filter(
            Q(user=request.user)
        )
        if len(validate_data) == 0:
            # Si no existe el registro, lo creamos
            user_general_id = UserGeneralGrades.objects.create(
                user=request.user,
                calf=round(final_prom_user, 2)
            )
        else:
            # Si el registro ya existe, lo actualizamos
            user_general_id = UserGeneralGrades.objects.filter(
                Q(user=request.user)
            ).update(
                user=request.user,
                calf=round(final_prom_user, 2)
            )
    # Obtenemos el promedio general del usuario
    user_prom_final = UserGeneralGrades.objects.filter(
        Q(user=request.user)
    )
    return render(request, "user_profile/profile.html",
                  {
                      'profile': profile,
                      'content': content,
                      'usersubs': usersubs,
                      'act': act,
                      'calfs': calfs,
                      'content_calf': course_calf,
                      'user_certs': user_certs,
                      'user_prom_final': user_prom_final
                  })

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