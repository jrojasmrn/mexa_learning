# Generated by Django 2.1.15 on 2021-01-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_testcourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentmedia',
            name='genially',
            field=models.URLField(blank=True, null=True, verbose_name='Link de Genially'),
        ),
    ]
