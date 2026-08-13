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
    path('departments', views.department_list),  # Fallback for links missing trailing slash
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/update/<int:dept_id>/', views.update_department, name='update_department'),
    path('departments/delete/<int:dept_id>/', views.delete_department, name='delete_department'),
    path('map-subjects/', views.map_subjects, name='map_subjects'),

    # Report URL
    path('report/', views.view_report, name='view_report'),
    path('report', views.view_report),  # Fallback for links missing trailing slash
    
    path('scores/', views.score_list, name='score_list'),
    path('scores/add/', views.add_score, name='add_score'), 
    path('scores/update/<int:score_id>/', views.update_score, name='update_score'),
    path('scores/delete/<int:score_id>/', views.delete_score, name='delete_score'),

    # Subject URLs
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects', views.subject_list),  # Fallback for links missing trailing slash
    path('subjects/add/', views.add_subject, name='add_subject'),
    path('subjects/update/<int:subject_id>/', views.update_subject, name='update_subject'),
    path('subjects/delete/<int:subject_id>/', views.delete_subject, name='delete_subject'),

]