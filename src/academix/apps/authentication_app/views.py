import json

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.views import View

from constants.error_messages import *
from constants.error_codes import *

from .service.service import (
    check_user_exists, 
    check_user_password,
    login_user_in_system, 
    send_otp_code_mail, 
    reset_password
)

class HomeView(View):
    def get(self, request):
        return render(request, 'index_auth.html')
    
class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'reset_password.html')
    
# ajax responses
def check_login(request) -> JsonResponse:
    username = request.POST.get('username')

    print(username)

    user = check_user_exists('username', username)

    if user is None:
        return JsonResponse({'status': 'error', 
                             'message': ERROR_USER_NOT_FOUND,
                             'error_code': ERROR_USER_NOT_FOUND_CODE})
    
    return JsonResponse({'status': 'success'})

def check_password(request) -> JsonResponse:
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = check_user_exists('username', username)

    if user is None:
        return JsonResponse({'status': 'error', 
                             'message': ERROR_USER_NOT_FOUND,
                             'error_code': ERROR_USER_NOT_FOUND_CODE})
    
    if not check_user_password(user, password):
        return JsonResponse({'status': 'error', 
                             'message': ERROR_USER_INCORRECT_PASSWORD,
                             'error_code': ERROR_USER_INCORRECT_PASSWORD_CODE})
    
    return JsonResponse({'status': 'success'})

def check_email(request) -> JsonResponse:
    email = request.POST.get('email')
    user = check_user_exists('email', email)

    if user is None:
        return JsonResponse({'status': 'error', 
                             'message': ERROR_USER_NOT_FOUND,
                             'error_code': ERROR_USER_NOT_FOUND_CODE})
    
    return JsonResponse({'status': 'success'})

def send_mail(request):
    email = request.POST.get('email')
    user = check_user_exists('email', email)

    reset_status = reset_password(user)

    if not reset_status:
        return JsonResponse({'status': 'error', 
                             'message': ERROR_USER_ERROR_RESET_PASSWORD,
                             'error_code': ERROR_USER_ERROR_RESET_PASSWORD_CODE})
    
    return JsonResponse({'status': 'success'})

def send_otp_code(request): 
    username = request.POST.get('username')

    user = check_user_exists('username', username)

    opt_send_status, otp_code = send_otp_code_mail(user.email)
    if not opt_send_status:
        return JsonResponse({'status': 'error', 
                             'message': ERROR_USER_ERROR_SEND_OTP,
                             'error_code': ERROR_USER_ERROR_SEND_OTP_CODE})
                             
    user.last_otp_code = otp_code
    user.save()
    
    return JsonResponse({'status': 'success'})

def check_otp_code(request): 
    username = request.POST.get('username')
    otp_code = int(request.POST.get('otp_code'))
 
    user = check_user_exists('username', username)
    expacted_otp_code = user.last_otp_code

    if otp_code != expacted_otp_code: 
       return JsonResponse({'status': 'error', 
                             'message': ERROR_USER_ERROR_CHECK_OTP,
                             'error_code': ERROR_USER_ERROR_CHECK_OTP_CODE})
    
    return JsonResponse({'status': 'success'})

def authenticate_user(request) -> JsonResponse:
    username = request.POST.get('username')

    user = check_user_exists('username', username)
    login(request, user)

    href = login_user_in_system(user)
    return JsonResponse({'status': 'success', 'href': href})