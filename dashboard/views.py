from django.shortcuts import render, redirect
from user_profile.models import UserCourse
from courses.models import ContentMedia, QuestionsTest, AnswersTest, AnsUserTest
from status.models import Status, StatusUserCourse
# Import . models
from .models import CheckMediaUser
from django.db.models import Q
#import forms
from .forms import UploadFile

# Create your views here.

# Checking module of course
def check_module_user(user, course, content_media):
    status = Status.objects.get(id=1)
    # Actualizamos el status del registro
    check_module_user_id = CheckMediaUser.objects.filter(
        Q(course=course),
        Q(content_media=content_media),
        Q(user=user)
    ).update(
        status=status
    )

# register course information to check function
def register_course(user, course):
    status = Status.objects.get(id=2)
    # Obtenemos el contenido media de los cursos
    media = ContentMedia.objects.filter(
        Q(content=course),
        Q(status=1)
    )
    # Iteramos en el contenido media
    for data in media:
        # Validamos que el registro no existe
        validate_data = CheckMediaUser.objects.values().filter(
            Q(course=course),
            Q(user=user),
            Q(content_media=data)
        )
        # Si no existe el registro, lo creamos
        if len(validate_data) == 0:
            check_media_id = CheckMediaUser.objects.create(
                content_media= data,
                course=course,
                user=user,
                status=status
            )
        # Si existe, lo actualizamos con la misma información
        else:
            check_media_user_id = CheckMediaUser.objects.filter(
                Q(course=course),
                Q(user=user),
                Q(content_media=data)
            ).update(
                content_media=data,
                course=course,
                user=user
            )

# Dashboard view
def dashboard(request, pk, course_name, pk_media):
    # Cambiamos el status del curso filtrando el curso por el ID
    instancia = UserCourse.objects.filter(
        Q(id=pk),
        Q(status=1) | Q(status=3)
    )
    for obj in instancia:
        new_status = StatusUserCourse.objects.get(status='En proceso')
        obj.status = new_status
        obj.save()
        # Obtengo el id del curso
        course_id = obj.course
    # Llenamos la tabla para hacer el check
    register_course(request.user, course_id)
    # Obtenemos el nombre de los cursos para mostrar
    content_course = CheckMediaUser.objects.filter(
        Q(course=course_id),
        Q(user=request.user)
    )
    #Validamos que existe examen para el curso
    val_exa = QuestionsTest.objects.filter(
        Q(content=course_id)
    )
    # Actualizamos status de la clase
    check_module_user(request.user, course_id, pk_media)
    # Obtenemos el contenido del curso filtrando por el id del curso obtenido
    content_course_data = ContentMedia.objects.filter(content=course_id, id=pk_media)
    # Función para mandar las actividades de usuarios
    form = UploadFile()
    if request.method == 'POST':
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('control-pane')
    return render(request, "dashboard/dashboard.html",
                {
                    'form': form,
                    'usercourse': instancia,
                    'content_course': content_course,
                    'content_course_data': content_course_data,
                    'val_exa': val_exa,
                })

# Test view
def tests(request, pk):
    # Obtenemos la información del examen
    question_data = QuestionsTest.objects.values().filter(
        Q(content=pk)
    ).order_by(
        'question'
    )
    answer_data = AnswersTest.objects.values().filter(
        Q(question__content=pk)
    ).order_by(
        'answer'
    )
    # Creamos una lista y dict vacios
    list_preguntas = []
    # Iteramos en las preguntas
    for data_q in question_data:
        # Agregamos la pregunta al dict
        dict_preguntas = {}
        dict_preguntas['question'] = data_q['question']
        count = 1
        # Iteramos en las respuestas
        for data_a in answer_data:
            # Validamos que la respuesta corresponda con la pregunta
            if data_q['id'] == data_a['question_id']:
                # Creamos un contador para aumentar el key del dict para las respuetas
                cont_answer = 'r_'+str(count)
                count += 1
                # Vamos agregando las respuestas con ayuda del contador
                dict_preguntas[cont_answer] = data_a['answer']
        # Agregamos el dict a una lista, para tener una lista de dicts
        list_preguntas.append(dict_preguntas)
    return render(request, "dashboard/exams.html", {'test': list_preguntas})