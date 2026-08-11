from django.contrib import admin
from .models import Student, Department, Subject, SemesterSubject

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'modified_on')
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_number', 'email', 'department', 'join_date')
    search_fields = ('name', 'roll_number', 'email')
    list_filter = ('department',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_code', 'subject_name')
    search_fields = ('subject_code', 'subject_name')

@admin.register(SemesterSubject)
class SemesterSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'department', 'semester', 'subject', 'created_on')
    list_filter = ('department', 'semester')
    search_fields = ('department__name', 'subject__subject_name', 'subject__subject_code')