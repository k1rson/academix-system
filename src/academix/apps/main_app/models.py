from django.contrib.auth.models import AbstractUser,  BaseUserManager
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар пользователя')
    last_otp_code = models.IntegerField(verbose_name='Последний OTP-код пользователя', null=True)

    def __str__(self):
        return f'{self.username}'
    
    class Meta: 
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class DisciplineModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    discipline_name = models.CharField(max_length=255, verbose_name='Название дисциплины', null=False)

    def __str__(self):
        return f'{self.discipline_name}'
    
    class Meta: 
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

class TeacherModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')
    is_teacher = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.full_name}'
    
    class Meta: 
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

class GroupModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_name = models.CharField(max_length=255, verbose_name='Название группы')
    amount_of_students = models.IntegerField(verbose_name='Общее количество студентов в группе')
    discipline_id = models.ForeignKey(DisciplineModel, on_delete=models.CASCADE, verbose_name='ID привязанных дисциплин')

    def __str__(self):
        return f'{self.id}, {self.group_name}, {self.amount_of_students}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class TeacherAssignmentsModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    teacher_id = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, verbose_name='ID Преподавателя')
    discipline_id = models.ForeignKey(DisciplineModel, on_delete=models.CASCADE, verbose_name='ID Дисциплины')

    def __str__(self):
        return f'{self.teacher_id}, {self.discipline_id}'
    
    class Meta: 
        verbose_name = 'Назначение преподавателей'
        verbose_name_plural = 'Назначение преподавателей'

class StudentModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')
    is_student = models.BooleanField(default=True)

    group_id = models.ForeignKey(GroupModel, on_delete=models.CASCADE, verbose_name='ID группы, к которой привязан студент')

    def __str__(self):
        return f'{self.full_name}, {self.group_id.group_name}'
    
    class Meta: 
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

