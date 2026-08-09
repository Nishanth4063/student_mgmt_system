from django import forms
from .models import Student, Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'dob', 'roll_number', 'email', 'join_date', 'department']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'join_date': forms.DateInput(attrs={'type': 'date'}),
        }