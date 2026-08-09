from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Department
from .forms import StudentForm, DepartmentForm
from datetime import date

# HOME - Student List
def home(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, 'home.html', {'students': students, 'active_tab': 'students'})

# ADD Student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

# UPDATE Student
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, instance=student)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'update_student.html', {'form': form})

# DELETE Student
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'delete_student.html', {'student': student})

# DETAIL Student
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    age = date.today().year - student.dob.year
    return render(request, 'student_detail.html', {'student': student, 'age': age})

# Department List
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments, 'active_tab': 'departments'})

# ADD Department
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})

# UPDATE Department
def update_department(request, dept_id):
    dept = get_object_or_404(Department, id=dept_id)
    form = DepartmentForm(request.POST or None, instance=dept)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('department_list')
    return render(request, 'update_department.html', {'form': form})

# DELETE Department
def delete_department(request, dept_id):
    dept = get_object_or_404(Department, id=dept_id)
    if request.method == 'POST':
        dept.delete()
        return redirect('department_list')
    return render(request, 'delete_department.html', {'dept': dept})

# VIEW REPORT
def view_report(request):
    departments = Department.objects.all()
    students = None
    selected_dept = request.GET.get('department')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    if selected_dept or from_date or to_date:
        students = Student.objects.all()
        if selected_dept:
            students = students.filter(department_id=selected_dept)
        if from_date:
            students = students.filter(join_date__gte=from_date)
        if to_date:
            students = students.filter(join_date__lte=to_date)

    return render(request, 'view_report.html', {
        'departments': departments,
        'students': students,
        'active_tab': 'report'
    })