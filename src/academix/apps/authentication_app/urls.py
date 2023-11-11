from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='login'),
    path('reset_password/', views.ResetPasswordView.as_view(), name='reset_password'),

    # ajax requests
    path('check_login/', views.check_login, name='check_login'),
    path('check_password/', views.check_password, name='check_password'),

    path('auth_user', views.authenticate_user, name='auth_user'),
    path('auth_user/send_opt_code', views.send_otp_code, name='send_otp_code'),
    path('auth_user/check_otp_code', views.check_otp_code, name='check_otp_code'),
    
    path('reset_password/check_email/', views.check_email, name='check_email'),
    path('reset_password/send_mail/', views.send_mail, name='check_email'),
]