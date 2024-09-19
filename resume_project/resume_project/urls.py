# resume_project/urls.py
from django.contrib import admin
from django.urls import path
from .views import resume_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/', resume_view, name='resume'),
]
