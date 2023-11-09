from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def student_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='Students').exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Доступ запрещен")

    return _wrapped_view

def teacher_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='Teachers').exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Доступ запрещен")

    return _wrapped_view
