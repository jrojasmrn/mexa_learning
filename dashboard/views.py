from django.shortcuts import render, redirect
from user_profile.models import UserCourse, UserCourseGrade, UserCertificates
from courses.models import ContentHeader, ContentMedia, QuestionsTest, AnswersTest, AnsUserTest
from status.models import Status, StatusUserCourse, UserGradeStatus
from django.contrib.auth.models import User
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
        dict_preguntas['id'] = data_q['id']
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
    # Obtenemos las respuestas del usuario
    # Comprobamos si la respuesta es un POST
    if request.method == 'POST':
        # Hacemos un loop del numero de preguntas
        for cant_p in list_preguntas:
            # Obtenemos la pregunta
            user_question = request.POST.get(''+str(cant_p['id']))
            question_instance = QuestionsTest.objects.get(id=user_question)
            # Obtengo la respuesta del usuario
            user_ans = request.POST.get('select_'+str(cant_p['id']))
            answer_instance = AnswersTest.objects.get(answer=user_ans)
            # Obtenemos instancia de curso
            user_course = ContentHeader.objects.get(id=pk)
            # Validamos que el registro no exista
            validate_data = AnsUserTest.objects.values().filter(
                Q(user=request.user),
                Q(course=user_course)
            )
            if len(validate_data) == 0:
                # Creamos el registro en la tabla
                ans_user_id = AnsUserTest.objects.create(
                    answer=answer_instance,
                    course=user_course,
                    user=request.user,
                    question=question_instance
                )
            else:
                # Actualizamos los registros del usuario
                ans_user_id = AnsUserTest.objects.filter(
                    Q(user=request.user),
                    Q(course=user_course)
                ).update(
                    answer=answer_instance,
                    course=user_course,
                    user=request.user,
                    question=question_instance
                )
            return redirect('user_results', pk)
    return render(request, "dashboard/exams.html", {'test': list_preguntas})

# Create certificate function
def create_certificate(user, content):
    # Reprot Lab library
    from reportlab.pdfgen import canvas

    # Obtenemos la información de la calf
    user_calf = UserCourseGrade.objects.filter(
        Q(user=user),
        Q(content=content)
    )
    for data in user_calf:
        cert_user = data.user.get_full_name()
        cert_course = data.content.title
        cert_date = data.created
        # Creamos un identificador para el nombre del certificado
        cert_id = '%s_%s' % (data.user.id, data.content.id)
    # PDF Content:
    filename = 'certificate_%s.pdf' % (cert_id)
    documenttitle = 'Certificado de termino -' + cert_user
    title = 'Otorga a'
    user = '' + cert_user
    label_course = 'El siguiente certificado, por acreditar con éxito el curso de'
    course_name = '' + cert_course
    create_date = 'Otorgado el día ' + str(cert_date)
    congra_text = 'Por parte del equipo de Mexamerik, te felicitamos por seguir aprendiendo en cada momento.'
    ceo_name = 'Lic. Pablo Ocampo'
    rh_manager = 'Lic. Jorge N'
    image = 'core/static/core/img/logo_mexa.jpg'
    ceo_sig = 'core/static/core/img/firma.jpg'
    rh_sig = 'core/static/core/img/firma.jpg'

    # Step 0: create the pdf file
    pdf = canvas.Canvas('media/'+filename)
    pdf.setTitle(documenttitle)

    # Step 1: Image logo
    pdf.drawInlineImage(image, 45, 600)

    # Step 2: Title
    # Register a new font
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase import pdfmetrics
    pdfmetrics.registerFont(
        TTFont('berkshire', 'core/static/core/fonts/berkshire/Berkshire.ttf')
    )
    # Set the principal font
    pdf.setFont('berkshire', 18)
    # Print the title
    pdf.drawCentredString(300, 550, title)

    # Step 3: Username
    # Set the principal font
    pdf.setFont('berkshire', 25)
    pdf.drawCentredString(300, 500, user)

    # Step 4: Label course
    # Set the principal font
    pdf.setFont('berkshire', 18)
    pdf.drawCentredString(300, 450, label_course)

    # Step 5: Course name
    # Set the principal font
    pdf.setFont('berkshire', 25)
    pdf.drawCentredString(300, 400, course_name)

    # Step 6: created date
    # Set the principal font
    pdf.setFont('berkshire', 14)
    pdf.drawCentredString(300, 360, create_date)

    # Step 7: Congratulations text
    # Set the principal font
    pdf.setFont('berkshire', 12)
    pdf.drawCentredString(300, 300, congra_text)

    # Step 8: CEO's name
    # Set the principal font
    pdf.setFont('berkshire', 10)
    pdf.drawInlineImage(ceo_sig, 100, 120, width=100, height=60)
    pdf.drawInlineImage(rh_sig, 420, 120, width=100, height=60)
    pdf.drawString(100, 100, ceo_name)
    pdf.drawString(450, 100, rh_manager)

    # Save the document
    pdf.save()

# Results view
def user_results(request, pk):
    # Obtenemos respuestas del usuario
    user_ans = AnsUserTest.objects.filter(
        Q(user=request.user),
        Q(course=pk)
    )
    # Calculamos la calificacion del usuario
    c_ans = 0
    status = 1
    for ans_data in user_ans:
        # Validamos que la respuesta sea correcta
        if ans_data.answer.is_correct == True:
            c_ans += 1
    calf_final = (c_ans * 10)/len(user_ans)
    # Si la calificacion es menor o igual a 6, se coloca 5
    if calf_final <= 6:
        calf_final = 5
        status = 2
    # Obtenemos la instancia de los datos para hacer el registro
    content_instance = ContentHeader.objects.get(id=pk)
    status_instance = UserGradeStatus.objects.get(id=status)
    # Validamos que no exista el registro
    validate_data = UserCourseGrade.objects.values().filter(
        Q(content=pk),
        Q(user=request.user)
    )
    # Si no existe el registro, lo creamos
    if len(validate_data) == 0:
        user_grade_id = UserCourseGrade.objects.create(
            calf=calf_final,
            content=content_instance,
            status=status_instance,
            user=request.user
        )
    # Si existe, lo actualizamos
    else:
        user_grade_id = UserCourseGrade.objects.filter(
            Q(content=pk),
            Q(user=request.user)
        ).update(
            calf=calf_final,
            content=content_instance,
            status=status_instance,
            user=request.user
        )
    # Obtenemos calificacion del usuario
    user_grade_info = UserCourseGrade.objects.filter(
        Q(content=pk),
        Q(user=request.user)
    )
    # Iteramos en la informacion del usuario
    for data_calf in user_grade_info:
        validate_calf = data_calf.calf
        # Si el usaurio aprobó el curso
        if validate_calf != '5':
            # Generamos el certificado del usuario
            create_certificate(request.user, pk)
            # Cambiamos de status el curso del usuario
            new_status_instance = StatusUserCourse.objects.get(id=4)
            user_course_id = UserCourse.objects.filter(
                Q(course=pk),
                Q(user=request.user)
            ).update(
                status=new_status_instance
            )
            # Insertamos el documento en la tabla
            # Validamos que el registro no exista
            validate_data = UserCertificates.objects.values().filter(
                Q(user=request.user),
                Q(content=pk)
            )
            # Si no existe, lo insertamos
            if len(validate_data) == 0:
                # Creamos el mismo nombre del documento
                # Creamos un identificador para el nombre del certificado
                cert_id = '%s_%s' % (request.user.id, pk)
                filename = 'certificate_%s.pdf' % (cert_id)
                user_cert_id = UserCertificates.objects.create(
                    cert_file=filename,
                    content=content_instance,
                    user=request.user
                )
    # Obtenemos el certificado del usuario
    user_cert_pdf = UserCertificates.objects.filter(
        Q(content=pk),
        Q(user=request.user)
    )

    return render(request, "dashboard/results.html", {'user_ans': user_ans, 'user_grade': user_grade_info, 'cert': user_cert_pdf})