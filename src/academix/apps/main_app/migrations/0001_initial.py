# Generated by Django 4.2.7 on 2023-11-06 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplineModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('discipline_name', models.CharField(max_length=255, verbose_name='Название дисциплины')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=255, verbose_name='Название группы')),
                ('amount_of_students', models.IntegerField(verbose_name='Общее количество студентов в группе')),
                ('discipline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.disciplinemodel', verbose_name='ID привязанных дисциплин')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=255, verbose_name='Отчество')),
                ('full_name', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('is_teacher', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='TeacherAssignmentsModel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('discipline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.disciplinemodel', verbose_name='ID Дисциплины')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.teachermodel', verbose_name='ID Преподавателя')),
            ],
            options={
                'verbose_name': 'Назначение преподавателей',
                'verbose_name_plural': 'Назначение преподавателей',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=255, verbose_name='Отчество')),
                ('full_name', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('is_student', models.BooleanField(default=True)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.groupmodel', verbose_name='ID группы, к которой привязан студент')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]
