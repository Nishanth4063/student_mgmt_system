from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .forms import StudentForm, DepartmentForm, SubjectForm, ScoreForm
from .models import Student, Department, Subject, SemesterSubject, Score


# ==========================================
# 1. STUDENT MANAGEMENT
# ==========================================

# HOME - Student List
def home(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query).select_related('department')
    else:
        students = Student.objects.all().select_related('department')
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
    if request.method == 'POST' and form.is_valid():
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
    today = date.today()
    age = today.year - student.dob.year - ((today.month, today.day) < (student.dob.month, student.dob.day))
    return render(request, 'student_detail.html', {'student': student, 'age': age})


# ==========================================
# 2. DEPARTMENT MANAGEMENT
# ==========================================

# DEPARTMENT LIST
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
    if request.method == 'POST' and form.is_valid():
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


# ==========================================
# 3. SUBJECT MANAGEMENT
# ==========================================

# SUBJECT LIST
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects, 'active_tab': 'subjects'})


# ADD SUBJECT
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'add_subject.html', {'form': form})


# UPDATE SUBJECT
def update_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    form = SubjectForm(request.POST or None, instance=subject)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('subject_list')
    return render(request, 'update_subject.html', {'form': form})


# DELETE SUBJECT
def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'delete_subject.html', {'subject': subject})


# ==========================================
# 4. SUBJECT MAPPING MODULE
# ==========================================

# MAP SUBJECTS TO SEMESTER
def map_subjects(request):
    departments = Department.objects.all()
    subjects = Subject.objects.all()

    selected_dept_id = request.GET.get('department')
    selected_sem = request.GET.get('semester')

    assigned_subjects = []
    assigned_subject_ids = []
    disabled_subject_ids = []

    selected_dept_id = int(selected_dept_id) if selected_dept_id and selected_dept_id.isdigit() else None
    selected_sem = int(selected_sem) if selected_sem and selected_sem.isdigit() else None

    if selected_dept_id:
        if selected_sem:
            current_mappings = SemesterSubject.objects.filter(
                department_id=selected_dept_id,
                semester=selected_sem
            ).select_related('subject')

            assigned_subject_ids = [m.subject_id for m in current_mappings]
            assigned_subjects = [m.subject for m in current_mappings]

            # Fetch subjects mapped to OTHER semesters, excluding current semester's subjects
            other_sem_mappings = SemesterSubject.objects.filter(
                department_id=selected_dept_id
            ).exclude(
                semester=selected_sem
            ).exclude(
                subject_id__in=assigned_subject_ids
            ).values_list('subject_id', flat=True)

            disabled_subject_ids = list(set(other_sem_mappings))
        else:
            all_dept_mappings = SemesterSubject.objects.filter(
                department_id=selected_dept_id
            ).values_list('subject_id', flat=True)
            disabled_subject_ids = list(set(all_dept_mappings))

    if request.method == 'POST':
        dept_id = request.POST.get('department')
        sem = request.POST.get('semester')
        chosen_subject_ids = request.POST.getlist('subjects')

        if not (dept_id and sem and dept_id.isdigit() and sem.isdigit()):
            return redirect('map_subjects')

        dept_id = int(dept_id)
        sem = int(sem)

        other_sem_mappings = SemesterSubject.objects.filter(
            department_id=dept_id
        ).exclude(
            semester=sem
        ).values_list('subject_id', flat=True)

        forbidden_ids = set(other_sem_mappings)

        valid_subject_ids = [
            int(sub_id) for sub_id in chosen_subject_ids
            if sub_id.isdigit() and int(sub_id) not in forbidden_ids
        ]

        with transaction.atomic():
            SemesterSubject.objects.filter(department_id=dept_id, semester=sem).delete()
            new_mappings = [
                SemesterSubject(department_id=dept_id, semester=sem, subject_id=sub_id)
                for sub_id in valid_subject_ids
            ]
            SemesterSubject.objects.bulk_create(new_mappings)

        return redirect(f"/map-subjects/?department={dept_id}&semester={sem}")

    return render(request, 'map_subjects.html', {
        'departments': departments,
        'subjects': subjects,
        'semesters': range(1, 9),
        'selected_dept': selected_dept_id,
        'selected_sem': selected_sem,
        'assigned_subject_ids': assigned_subject_ids,
        'assigned_subjects': assigned_subjects,
        'disabled_subject_ids': disabled_subject_ids,
        'active_tab': 'departments'
    })


# ==========================================
# 5. SCORES MANAGEMENT MODULE
# ==========================================

# SCORE LIST
def score_list(request):
    scores = Score.objects.select_related('student', 'subject').all()
    return render(request, 'score_list.html', {
        'scores': scores,
        'active_tab': 'scores'
    })


# ADD SCORE (SMART MARKS ENTRY)
def add_score(request):
    students = Student.objects.select_related('department').all()

    selected_student_id = request.GET.get('student')
    selected_sem = request.GET.get('semester')

    selected_student = None
    mapped_subjects = []

    # Safe conversion from string/int inputs
    student_pk = int(selected_student_id) if selected_student_id and str(selected_student_id).isdigit() else None
    sem_num = int(selected_sem) if selected_sem and str(selected_sem).isdigit() else None

    # Step 1: Detect Student & Department
    if student_pk:
        selected_student = get_object_or_404(Student, id=student_pk)

        # Step 2: Fetch subjects mapped explicitly to Student's Dept + Selected Semester
        if sem_num:
            subject_ids = SemesterSubject.objects.filter(
                department=selected_student.department,
                semester=sem_num
            ).values_list('subject_id', flat=True)

            mapped_subjects = Subject.objects.filter(id__in=subject_ids)

    # Step 3: Handle Score Submission (POST)
    if request.method == 'POST':
        student_id = request.POST.get('student')
        semester = request.POST.get('semester')

        if student_id and semester:
            student = get_object_or_404(Student, id=student_id)

            with transaction.atomic():
                for key, value in request.POST.items():
                    if key.startswith('marks_') and value.strip() != '':
                        subject_id = key.split('_')[1]
                        marks = float(value)

                        Score.objects.update_or_create(
                            student=student,
                            subject_id=subject_id,
                            defaults={'marks': marks}
                        )
            return redirect('score_list')

    return render(request, 'add_score.html', {
        'students': students,
        'selected_student': selected_student,
        'selected_sem': sem_num,
        'mapped_subjects': mapped_subjects,
        'semesters': range(1, 9),
        'active_tab': 'scores'
    })

# UPDATE SCORE
def update_score(request, score_id):
    score = get_object_or_404(Score, id=score_id)
    
    # 1. Get all subject IDs mapped to this student's department across all semesters
    department_subject_ids = SemesterSubject.objects.filter(
        department=score.student.department
    ).values_list('subject_id', flat=True)

    form = ScoreForm(request.POST or None, instance=score)
    
    # 2. Filter the Subject dropdown to ONLY show subjects belonging to the student's department
    form.fields['subject'].queryset = Subject.objects.filter(id__in=department_subject_ids)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('score_list')

    return render(request, 'update_score.html', {
        'form': form, 
        'score': score,
        'active_tab': 'scores'
    })

# DELETE SCORE
def delete_score(request, score_id):
    score = get_object_or_404(Score, id=score_id)
    if request.method == 'POST':
        score.delete()
        return redirect('score_list')
    return render(request, 'delete_score.html', {'score': score})


# ==========================================
# 6. REPORTING MODULE
# ==========================================

# VIEW REPORT
def view_report(request):
    departments = Department.objects.all()
    students = None
    selected_dept = request.GET.get('department')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    if selected_dept or from_date or to_date:
        students = Student.objects.select_related('department').all()
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