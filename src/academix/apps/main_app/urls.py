from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='home_main_page'),
]