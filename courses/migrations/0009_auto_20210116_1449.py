# Generated by Django 2.1.15 on 2021-01-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_contentmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentmedia',
            name='description',
            field=models.TextField(blank=True, default='No hay descripción', null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='contentmedia',
            name='notes',
            field=models.TextField(blank=True, default='No hay notas', null=True, verbose_name='Notas'),
        ),
    ]
