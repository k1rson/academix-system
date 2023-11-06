from django.contrib.auth.models import AbstractUser, Group, Permission

from django.db import models

# fix bad imports
#from ...main_app.models import TeacherModel

class DisciplineModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    discipline_name = models.CharField(max_length=255, verbose_name='Название дисциплины', null=False)

class TeacherAssignmentsModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    #teacher_id = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, verbose_name='ID Преподавателя')
    discipline_id = models.ForeignKey(DisciplineModel, on_delete=models.CASCADE, verbose_name='ID Дисциплины')