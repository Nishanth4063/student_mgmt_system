from django.db import models
from django.utils import timezone
from datetime import date


# 1. Department Model
class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    modified_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# 2. Student Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    roll_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100)
    join_date = models.DateField(null=True)
    department = models.ForeignKey(
        'students.Department',
        on_delete=models.SET_NULL,
        null=True
    )

    def get_age(self):
        if self.dob:
            today = date.today()
            years = today.year - self.dob.year
            months = today.month - self.dob.month
            if months < 0:
                years -= 1
                months += 12
            return f"{years}y {months}m"
        return "N/A"

    def __str__(self):
        return self.name


# 3. Subject Model
class Subject(models.Model):
    subject_name = models.CharField(max_length=150)
    subject_code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"


# 4. Department + Semester + Subject Mapping Model
class SemesterSubject(models.Model):
    SEMESTER_CHOICES = [(i, f"Semester {i}") for i in range(1, 9)]

    department = models.ForeignKey('students.Department', on_delete=models.CASCADE)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    subject = models.ForeignKey('students.Subject', on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('department', 'semester', 'subject')

    def __str__(self):
        return f"{self.department.name} - Sem {self.semester} - {self.subject.subject_code}"