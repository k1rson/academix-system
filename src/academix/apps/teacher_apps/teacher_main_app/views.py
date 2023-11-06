from django.shortcuts import render

from django.views import View

class TeachWorkSpaceView(View):
    def get(self, request):
        return render(request, 'index_teach.html')