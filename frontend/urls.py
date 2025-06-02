from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('subjects/', views.subject_list, name='subject_list'),
]