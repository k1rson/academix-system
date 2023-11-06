from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.TeachWorkSpaceView.as_view(), name='teacher_work_space')
]