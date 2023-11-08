from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='login'),

    # ajax requests
    path('check_login/', views.check_login, name='check_login'),
    path('check_password/', views.check_password, name='check_password'),
    path('auth_user/', views.authenticate_user, name='authenticate_user'),
]