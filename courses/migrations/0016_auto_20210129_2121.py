# Generated by Django 2.1.15 on 2021-01-30 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_answertestcourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answertestcourse',
            name='question',
        ),
        migrations.RemoveField(
            model_name='testcourse',
            name='content',
        ),
        migrations.DeleteModel(
            name='AnswerTestCourse',
        ),
        migrations.DeleteModel(
            name='TestCourse',
        ),
    ]
