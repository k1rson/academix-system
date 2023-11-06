from django.contrib.auth.models import AbstractUser, User

from django.db import models

# конченные import's - пофиксить
from ...teacher_apps.teacher_main_app.models import DisciplineModel

class GroupModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_name = models.CharField(max_length=255, verbose_name='Название группы')
    amount_of_students = models.IntegerField(verbose_name='Общее количество студентов в группе')
    discipline_id = models.ForeignKey(DisciplineModel, on_delete=models.CASCADE, verbose_name='ID привязанных дисциплин(-ы)')

    def __str__(self):
        return f'{self.id}, {self.group_name}, {self.amount_of_students}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class StudentModel(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, verbose_name='Логин студента', null=False)
    first_name = models.CharField(max_length=255, verbose_name='Имя студента', null=False)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия студента', null=False)
    middle_name = models.CharField(max_length=255, verbose_name='Отчество студента', null=True)
    full_name = models.CharField(max_length=255, verbose_name='Полное имя', null=True)
    group_id = models.ForeignKey(GroupModel, on_delete=models.CASCADE, verbose_name='Группа, которой привязан студент')

    def __str__(self):
        return f'{self.id}, {self.full_name}, {self.group_id}'
    
    class Meta:
        verbose_name_plural = 'Студенты'