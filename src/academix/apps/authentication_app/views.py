import json

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.views import View

from constants.error_messages import *
from constants.error_codes import *

from .decorators import student_required, teacher_required

from .service.service import (
    check_user_exists, 
    check_user_password
)

class HomeView(View):
    def get(self, request):
        return render(request, 'index_auth.html')
    
# ajax responses
def check_login(request) -> JsonResponse:
    username = request.POST.get('username')
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

@student_required
def authenticate_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    print(username, password)

    user = check_user_exists('username', username)

    print(user)
    print(login(request, user))