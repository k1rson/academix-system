from django.contrib.auth.models import AbstractUser
from django.db import models

# fix import's
from ..student_apps.student_main_app.models import GroupModel

class CustomUser(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, verbose_name='Логин', unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')

class StudentModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_student = models.BooleanField(default=True)

    #group_id = models.ForeignKey(GroupModel, on_delete=models.CASCADE, verbose_name='ID группы, к которой привязан студент')

class TeacherModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=True)