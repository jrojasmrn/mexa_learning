# Generated by Django 2.1.15 on 2020-12-29 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
        ('courses', '0002_subscribecourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='', verbose_name='Imágen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='status.Status', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ModulesCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=254, verbose_name='Nombre de modulo')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Content', verbose_name='Contenido')),
            ],
            options={
                'verbose_name': 'Modulo',
                'verbose_name_plural': 'Modulos',
                'ordering': ['content'],
            },
        ),
    ]
