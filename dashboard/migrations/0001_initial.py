# Generated by Django 2.1.15 on 2021-01-25 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('status', '0001_initial'),
        ('courses', '0010_testcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckMediaUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.ContentMedia', verbose_name='Modulo')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.Status', verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Check de modulo',
                'verbose_name_plural': 'Check de modulos',
            },
        ),
    ]