from django.contrib import admin

from .models import StudentModel, TeacherModel, CustomUser

admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(CustomUser)