from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main_app.urls'), name='home'),
    path('auth/', include('apps.authentication_app.urls'), name='authentication'),
    path('std_workspace/', include('apps.student_apps.student_main_app.urls'), name='student_workspace'), 
    path('tch_workspace/', include('apps.teacher_apps.teacher_main_app.urls'), name='teacher_workspace'), 
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)