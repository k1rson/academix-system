from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from django.views import View

class HomeView(View):
    def get(self, request): 
        return render(request, 'index.html')