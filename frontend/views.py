from django.shortcuts import render, redirect
import requests
from django.contrib import messages

API_BASE_URL = 'https://juvert12321.pythonanywhere.com/api/'

def index(request):
    return render(request, 'frontend/index.html')

def student_list(request):
    response = requests.get(f'{BASE_API_URL}students/')
    students = response.json() if response.status_code == 200 else []
    return render(request, 'frontend/student_list.html', {'students': students})

def student_detail(request, student_id):
    # Get student
    student_response = requests.get(f'{BASE_API_URL}students/{student_id}/')
    student = student_response.json() if student_response.status_code == 200 else None
    
    # Get grades for this student
    grades_response = requests.get(f'{BASE_API_URL}grades/?student_id={student_id}')
    grades = grades_response.json() if grades_response.status_code == 200 else []
    
    # Get all subjects for dropdown
    subjects_response = requests.get(f'{BASE_API_URL}subjects/')
    subjects = subjects_response.json() if subjects_response.status_code == 200 else []
    
    context = {
        'student': student,
        'grades': grades,
        'subjects': subjects,
        'api_url': BASE_API_URL  # Add API URL to context
    }
    
    return render(request, 'frontend/student_detail.html', context)

def subject_list(request):
    response = requests.get(f'{BASE_API_URL}subjects/')
    subjects = response.json() if response.status_code == 200 else []
    return render(request, 'frontend/subject_list.html', {'subjects': subjects})