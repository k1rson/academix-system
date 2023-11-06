from django.contrib import admin

from .models import StudentModel, TeacherModel, GroupModel, DisciplineModel, TeacherAssignmentsModel

admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(GroupModel)
admin.site.register(DisciplineModel)
admin.site.register(TeacherAssignmentsModel)