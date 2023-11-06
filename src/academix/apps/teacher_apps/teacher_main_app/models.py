from django.contrib.auth.models import AbstractUser

from django.db import models

class TeacherModel(AbstractUser): 
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, verbose_name='Логин преподавателя', null=False)
    first_name = models.CharField(max_length=255, verbose_name='Имя преподавателя', null=False)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия преподавателя', null=False)
    middle_name = models.CharField(max_length=255, verbose_name='Отчество преподавателя', null=True)
    full_name = models.CharField(max_length=255, verbose_name='Полное имя преподавателя', null=True)

class DisciplineModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    discipline_name = models.CharField(max_length=255, verbose_name='Название дисциплины', null=False)

class TeacherAssignmentsModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    teacher_id = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, verbose_name='ID Преподавателя')
    discipline_id = models.ForeignKey(DisciplineModel, on_delete=models.CASCADE, verbose_name='ID Дисциплины')