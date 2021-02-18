# Generated by Django 2.1.15 on 2021-02-11 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogues', '0001_initial'),
        ('status', '0001_initial'),
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityGrades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
            ],
            options={
                'verbose_name': 'Calificaciones de actividades',
                'verbose_name_plural': 'Calificaciones de actividades',
            },
        ),
        migrations.CreateModel(
            name='ActivityUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_file', models.FileField(upload_to='', verbose_name='Archivo')),
                ('comment', models.TextField(verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.ContentHeader', verbose_name='Nombre de curso')),
                ('content_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.ContentMedia', verbose_name='Nombre de contenido')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Actividad usuario',
                'verbose_name_plural': 'Actividades usuarios',
            },
        ),
        migrations.CreateModel(
            name='UserCertificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_file', models.CharField(max_length=254, verbose_name='Certificado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.ContentHeader', verbose_name='Contenido')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Certificado',
                'verbose_name_plural': 'Certificados',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.ContentHeader', verbose_name='Nombre de curso')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='status.StatusUserCourse', verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nombre de usuario')),
            ],
            options={
                'verbose_name': 'Curso de usuario',
                'verbose_name_plural': 'Cursos de usuarios',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='UserCourseGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calf', models.CharField(max_length=254, verbose_name='Calificacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.ContentHeader', verbose_name='Curso')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.UserGradeStatus', verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Calificaciones de curso',
                'verbose_name_plural': 'Calificaciones de cursos',
            },
        ),
        migrations.CreateModel(
            name='UserGeneralGrades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calf', models.FloatField(verbose_name='Calificacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Promedio general',
                'verbose_name_plural': 'Promedios generales',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción del usuario')),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imágen de usuario')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('languaje', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogues.LanguajeList', verbose_name='Lenguaje')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogues.StatesList', verbose_name='Estado')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nombre de usuario')),
            ],
            options={
                'verbose_name': 'Perfil de usuario',
                'verbose_name_plural': 'Perfiles de usuarios',
            },
        ),
        migrations.AddField(
            model_name='activitygrades',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.ActivityUsers', verbose_name='Actividad'),
        ),
        migrations.AddField(
            model_name='activitygrades',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.ContentHeader', verbose_name='Curso'),
        ),
        migrations.AddField(
            model_name='activitygrades',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogues.UserGrades', verbose_name='Calificacion'),
        ),
        migrations.AddField(
            model_name='activitygrades',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]