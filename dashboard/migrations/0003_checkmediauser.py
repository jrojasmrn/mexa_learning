# Generated by Django 2.1.15 on 2021-01-26 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0010_testcourse'),
        ('status', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_auto_20210125_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckMediaUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.ContentMedia', verbose_name='Contenido')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.ContentHeader', verbose_name='Curso')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.Status', verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Check de modulo',
                'verbose_name_plural': 'Check de modulos',
            },
        ),
    ]