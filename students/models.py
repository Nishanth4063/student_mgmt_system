from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    roll_number=models.CharField(max_length=20,unique=True)
    email=models.EmailField()
    department=models.CharField(max_length=50)
    join_date=models.DateField()

    def __str__(self):
        return self.name