from django.db import models
from django.utils import timezone
from datetime import date

# Department Table
class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    modified_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# Student Table
class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    roll_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100)
    join_date = models.DateField(null=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True
    )

    def get_age(self):
        today = date.today()
        years = today.year - self.dob.year
        months = today.month - self.dob.month
        if months < 0:
            years -= 1
            months += 12
        return f"{years}y {months}m"

    def __str__(self):
        return self.name