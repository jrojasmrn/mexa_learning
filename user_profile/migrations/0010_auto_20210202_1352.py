# Generated by Django 2.1.15 on 2021-02-02 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0017_ansusertest_question'),
        ('user_profile', '0009_usercoursegrade'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCertificates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_file', models.FileField(upload_to='', verbose_name='Certificado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.ContentHeader', verbose_name='Contenido')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Certificado',
                'verbose_name_plural': 'Certificados',
            },
        ),
        migrations.AlterModelOptions(
            name='activitygrades',
            options={'verbose_name': 'Calificaciones de actividades', 'verbose_name_plural': 'Calificaciones de actividades'},
        ),
    ]
