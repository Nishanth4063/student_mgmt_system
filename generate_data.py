import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_mgmt.settings')
django.setup()

from students.models import Student, Department

# Create Departments first
departments_data = [
    {'name': 'CSE', 'description': 'Computer Science Engineering'},
    {'name': 'IT', 'description': 'Information Technology'},
    {'name': 'ECE', 'description': 'Electronics and Communication'},
    {'name': 'EEE', 'description': 'Electrical and Electronics'},
    {'name': 'MECH', 'description': 'Mechanical Engineering'},
    {'name': 'CIVIL', 'description': 'Civil Engineering'},
]

# Create departments
for d in departments_data:
    Department.objects.get_or_create(name=d['name'], defaults={'description': d['description']})

print("Departments created!")

# Get all departments
depts = list(Department.objects.all())

# Indian names
first_names = [
    'Rahul', 'Priya', 'Arun', 'Sneha', 'Vikram',
    'Meera', 'Karthik', 'Divya', 'Anil', 'Pooja',
    'Suresh', 'Kavitha', 'Ravi', 'Lakshmi', 'Ganesh',
    'Deepa', 'Murugan', 'Anitha', 'Selvam', 'Nisha',
    'Ramesh', 'Geetha', 'Kumar', 'Revathi', 'Siva',
]

last_names = [
    'Kumar', 'Sharma', 'Raj', 'Singh', 'Nair',
    'Reddy', 'Iyer', 'Menon', 'Gupta', 'Verma',
    'Pillai', 'Das', 'Bose', 'Murugan', 'Pandian',
]

# Generate 100 students
for i in range(1, 101):
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"

    # Random DOB between 1998 and 2004
    start_date = date(1998, 1, 1)
    end_date = date(2004, 12, 31)
    dob = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    # Random join date between 2018 and 2024
    join_start = date(2018, 1, 1)
    join_end = date(2024, 12, 31)
    join_date = join_start + timedelta(days=random.randint(0, (join_end - join_start).days))

    roll = f"ROLL{str(i).zfill(3)}"
    email = f"{first.lower()}.{last.lower()}{i}@email.com"
    dept = random.choice(depts)

    Student.objects.create(
        name=name,
        dob=dob,
        roll_number=roll,
        email=email,
        join_date=join_date,
        department=dept
    )
    print(f"Created: {name}")

print("\nDone! 100 students created! ✅")