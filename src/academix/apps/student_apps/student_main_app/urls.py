from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentWorkSpaceView.as_view(), name='student_work_space'), 
]