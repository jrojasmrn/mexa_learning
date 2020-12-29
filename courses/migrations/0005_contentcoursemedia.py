# Generated by Django 2.1.15 on 2020-12-29 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
        ('catalogues', '0003_contenttype'),
        ('courses', '0004_auto_20201229_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentCourseMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Nombre de contenido')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('notes', models.TextField(default='No hay notas aún', verbose_name='Notas')),
                ('notices', models.TextField(default='No hay anuncios aquí', verbose_name='Anuncios')),
                ('g_suite', models.CharField(blank=True, max_length=254, null=True, verbose_name='Documentos Google')),
                ('video', models.URLField(blank=True, null=True, verbose_name='Video')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='', verbose_name='Seleccione documento PDF')),
                ('images', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Seleccione imágen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.ContentHeader', verbose_name='Nombre de curso')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogues.ContentType', verbose_name='Tipo de contenido')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.ModulesCourses', verbose_name='Nombre de módulo')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='status.Status', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Contenido de curso',
                'verbose_name_plural': 'Contenido de cursos',
                'ordering': ['content'],
            },
        ),
    ]