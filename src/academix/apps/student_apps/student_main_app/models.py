from django.db import models

# fix import's
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