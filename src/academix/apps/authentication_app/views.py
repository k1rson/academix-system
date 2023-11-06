import json

from django.contrib.auth import login
from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.views import View

from ..main_app.models import StudentModel

class HomeView(View):
    def get(self, request):
        return render(request, 'index_auth.html')
