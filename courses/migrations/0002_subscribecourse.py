# Generated by Django 2.1.15 on 2020-12-18 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe_time', models.DateTimeField(auto_now_add=True, verbose_name='Solicitado')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Content', verbose_name='Curso')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.Status', verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Suscripción',
                'verbose_name_plural': 'Suscripciones',
                'ordering': ['-subscribe_time'],
            },
        ),
    ]
