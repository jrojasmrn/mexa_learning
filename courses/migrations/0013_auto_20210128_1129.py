# Generated by Django 2.1.15 on 2021-01-28 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20210127_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribecourse',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.StatusSubscribeCourse', verbose_name='Status'),
        ),
    ]
