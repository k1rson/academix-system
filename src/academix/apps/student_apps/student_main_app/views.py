from django.shortcuts import render

from django.views import View

class StudentWorkSpaceView(View):
    def get(self, request):
        return render(request, 'index_stud.html')