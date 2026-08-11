"""
URL configuration for student_mgmt project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),  # Connects all application endpoints from students/urls.py
]