from django.urls import path
from . import views

urlpatterns = [
    # Student URLs
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),

    # Department URLs
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/update/<int:dept_id>/', views.update_department, name='update_department'),
    path('departments/delete/<int:dept_id>/', views.delete_department, name='delete_department'),

    # Report URL
    path('report/', views.view_report, name='view_report'),
]