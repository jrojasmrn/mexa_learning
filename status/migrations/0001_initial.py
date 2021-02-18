# Generated by Django 2.1.15 on 2021-02-11 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='StatusSubscribeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Subscribe course Status',
                'verbose_name_plural': 'Subscribe course Status',
            },
        ),
        migrations.CreateModel(
            name='StatusUserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'User course Status',
                'verbose_name_plural': 'User course Status',
            },
        ),
        migrations.CreateModel(
            name='UserGradeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Course grade Status',
                'verbose_name_plural': 'Course grade Status',
            },
        ),
    ]