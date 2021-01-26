from django.shortcuts import render, redirect
from django.db.models import Q
# Import User profile models
from user_profile.models import UserProfile, UserCourse, ActivityUsers
# Import Content models
from courses.models import ContentHeader, ContentMedia, SubscribeCourse
# Import Status model
from status.models import Status
# Import core models
from core.models import Advertisements, AssistanceUser
# Import dashboard models
from dashboard.models import CheckMediaUser
# Import forms
from .forms import *

# Create your views here.

# Admin Panel View
def admin_panel(request):
    return render(request, "admin_panel/admin_panel.html")

# Users view
def users_panel(request):
    # Obtenemos la lista de usuarios
    queryset_name = request.GET.get("buscar")
    users = User.objects.all()
    # Hacemos el filtrado por nombre
    if queryset_name:
        users = User.objects.filter(
            Q(first_name__icontains = queryset_name)
        )
    # Obtenemos usuarios admin
    admin_users = User.objects.filter(is_staff=1)
    return render(request, "admin_panel/c_users.html", {'users': users, 'admin_users': admin_users})

# Create users view
def create_user(request):
    # Obtenemos el username del formulario
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    return render(request, "admin_panel/users_create.html", {'form': form})

# Update users view
def update_user(request, id_user):
    instancia = User.objects.get(id=id_user)
    form = UpdateUserForm(instance=instancia)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('users')
    return render(request, "admin_panel/users_update.html", {'form': form})

# Content Header view
def courses_header(request):
    # Obtenemos la lista de cursos
    queryset_name = request.GET.get("buscar")
    content = ContentHeader.objects.all()
    # Hacemos el filtrado por nombre
    if queryset_name:
        content = ContentHeader.objects.filter(
            Q(title__icontains=queryset_name)
        )
    return render(request, "admin_panel/c_courses.html", {'content': content})

# Create content header
def create_content(request):
    # Creamos un formulario vacio
    form = CreateCourseForm()
    # Validamos si se envía un formulario POST
    if request.method == 'POST':
        form = CreateCourseForm(request.POST, request.FILES)
        # Valido si mi form es valido
        if form.is_valid():
            form.save()
            return redirect('admin-courses')
    return render(request, "admin_panel/courses_create.html", {'form':form})

# Update content view
def update_content(request, id_course):
    instancia = ContentHeader.objects.get(id=id_course)
    form = UpdateCourseForm(instance=instancia)
    if request.method == 'POST':
        form = UpdateCourseForm(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            instancia.image = form.cleaned_data['image']
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('admin-courses')
    return render(request, "admin_panel/courses_update.html", {'form':form})

# Content media view
def content_media(request, id_course):
    # Mostramos el content_header para opción de modificar
    content = ContentHeader.objects.filter(id=id_course)
    # Obtenemos el contenido total dentro del curso
    media = ContentMedia.objects.filter(content=id_course)
    return render(request, "admin_panel/c_contet_media.html", {'preview':content, 'media':media})

# Create content media view
def create_media(request, id_course):
    #Obtenemos el curso por el id
    content = ContentHeader.objects.get(id=id_course)
    # Creamos formulario vacio
    form = CreateMediaForm()
    # Validamos si se envia un formulario POST
    if request.method == 'POST':
        form = CreateMediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-courses')
    return render(request, "admin_panel/media_create.html", {'form':form, 'content':content})

# Update content media view
def update_content_media(request, id_media):
    instancia = ContentMedia.objects.get(id=id_media)
    form = UpdateMediaForm(instance=instancia)
    if request.method == 'POST':
        form = UpdateMediaForm(request.POST, request.FILES, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('admin-courses')
    return render(request, "admin_panel/media_update.html", {'form':form})

# Accept user courses function
def accept_course(user, course):
    # Validamos que la solicitud exista para modificarla
    validate_data = SubscribeCourse.objects.values().filter(
        Q(user=user),
        Q(status=5),
        Q(course=course)
    )
    # Si el registro existe, se actualiza el campo de status
    if len(validate_data) > 0:
        subcribecourse_id = SubscribeCourse.objects.filter(
            Q(user=user),
            Q(status=5),
            Q(course=course)
        ).update(
            status=6
        )
        create_usercourse_fun(user, course)

# Refuse user course function
def refuse_course(user, course):
    # Validamos que la solicitud exista para modificarla
    validate_data = SubscribeCourse.objects.values().filter(
        Q(user=user),
        Q(status=5),
        Q(course=course)
    )
    # Si el registro existe, se actualiza el campo de status
    if len(validate_data) > 0:
        subcribecourse_id = SubscribeCourse.objects.filter(
            Q(user=user),
            Q(status=5),
            Q(course=course)
        ).update(
            status=7
        )

# Create user course function
def create_usercourse_fun(user, course):
    status = Status.objects.get(id=1)
    # Validamos que no exista el registro en la tabla
    validate_data = UserCourse.objects.values().filter(
        Q(user=user),
        Q(course=course)
    )
    # Si el registro no existe, se crea uno nuevo
    if len(validate_data) == 0:
        usercourse_id = UserCourse.objects.create(
            user=user,
            course=course,
            status=status
        )
# User Subscribe view
def subs_control(request):
    #Obtengo las solicitudes de los cursos
    sols = SubscribeCourse.objects.filter(status=5)
    # Obtengo todos los cursos de los usuarios
    queryset_name = request.GET.get('buscar')
    user_course = UserCourse.objects.all()
    # Hacemos el filtrado por nombre
    if queryset_name:
        user_course = UserCourse.objects.filter(
            Q(user__first_name__icontains=queryset_name)
        )
    # Recibimos valor de flag y validamos si el curso se acepta o no
    queryset_flag = request.GET.get('flag')
    if queryset_flag:
        if queryset_flag == '1':
            for data in sols:
                accept_course(data.user, data.course)
                return redirect('user_subs')
        elif queryset_flag == '2':
            for data in sols:
                refuse_course(data.user, data.course)
                return redirect('user_subs')
    return render(request, "admin_panel/c_subs.html", {'user_c': user_course, 'sols':sols})

# Create User-Course view
def create_user_course(request):
    form = AssignCourseForm()
    # Validamos si se envía un formulario POST
    if request.method == 'POST':
        form = AssignCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_subs')
    return render(request, "admin_panel/subs_create.html", {'form': form})

# Update User-course view
def update_user_course(request, pk):
    instancia = UserCourse.objects.get(id=pk)
    form = UpdateAssignCourseForm(instance=instancia)
    if request.method == 'POST':
        form = UpdateAssignCourseForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('user_subs')
    return render(request, "admin_panel/subs_update.html", {'form': form})

# Notices control view
def notices_users(request):
    notices = Advertisements.objects.all()
    return render(request, "admin_panel/c_notices.html", {'notices': notices})

# Create notice view
def create_notice(request):
    form = CreateAdvertisementForm()
    # Validamos que formulario sea POST
    if request.method == 'POST':
        form = CreateAdvertisementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-panel')
    return render(request, "admin_panel/notices_create.html", {'form': form})

# Update notice view
def update_notice(request, id_notice):
    instancia = Advertisements.objects.get(id=id_notice)
    form = UpdateAdvertisementsForm(instance=instancia)
    if request.method == 'POST':
        form = UpdateAdvertisementsForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('admin-panel')
    return render(request, "admin_panel/notices_update.html", {'form': form})

# Activity user control view
def assistment_user(request, id_user):
    assist = AssistanceUser.objects.filter(user=id_user)
    info = UserProfile.objects.filter(user=id_user)
    user_course = UserCourse.objects.filter(user=id_user)
    act_user = ActivityUsers.objects.filter(user=id_user)
    return render(request, "admin_panel/c_assistment.html", {'assist': assist, 'profile': info, 'course': user_course, 'act':act_user})