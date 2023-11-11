from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import StudentModel, TeacherModel, GroupModel, DisciplineModel, TeacherAssignmentsModel, CustomUser

admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(GroupModel)
admin.site.register(DisciplineModel)
admin.site.register(TeacherAssignmentsModel)
admin.site.register(CustomUser, UserAdmin)