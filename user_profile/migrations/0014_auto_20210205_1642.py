# Generated by Django 2.1.15 on 2021-02-05 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0013_usergeneralgrades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergeneralgrades',
            name='calf',
            field=models.FloatField(verbose_name='Calificacion'),
        ),
    ]
