from django.shortcuts import render, redirect
import requests
from django.contrib import messages

API_BASE_URL = 'https://juvert12321.pythonanywhere.com/api/'

def index(request):
    return render(request, 'frontend/index.html')

def student_list(request):
    print(">>> student_list view called")  # Server-side debug
    try:
        response = requests.get(f'{API_BASE_URL}students/', timeout=5)
        response.raise_for_status()
        students = response.json()
    except Exception as e:
        print(">>> Error fetching students:", e)
        students = []
        messages.error(request, "Could not load student data. Please try again later.")
    return render(request, 'frontend/student_list.html', {'students': students})

def student_detail(request, student_id):
    print(f">>> student_detail view called for student_id={student_id}")
    student = None
    grades = []
    subjects = []

    try:
        student_response = requests.get(f'{API_BASE_URL}students/{student_id}/', timeout=5)
        student_response.raise_for_status()
        student = student_response.json()
    except Exception as e:
        print(">>> Error fetching student details:", e)
        messages.error(request, "Could not load student details.")

    try:
        grades_response = requests.get(f'{API_BASE_URL}grades/?student_id={student_id}', timeout=5)
        grades_response.raise_for_status()
        grades = grades_response.json()
    except Exception as e:
        print(">>> Error fetching grades:", e)
        messages.error(request, "Could not load student grades.")

    try:
        subjects_response = requests.get(f'{API_BASE_URL}subjects/', timeout=5)
        subjects_response.raise_for_status()
        subjects = subjects_response.json()
    except Exception as e:
        print(">>> Error fetching subjects:", e)
        messages.error(request, "Could not load subjects.")

    context = {
        'student': student,
        'grades': grades,
        'subjects': subjects,
        'api_url': API_BASE_URL
    }

    return render(request, 'frontend/student_detail.html', context)

def subject_list(request):
    print(">>> subject_list view called")
    try:
        response = requests.get(f'{API_BASE_URL}subjects/', timeout=5)
        response.raise_for_status()
        subjects = response.json()
    except Exception as e:
        print(">>> Error fetching subjects:", e)
        subjects = []
        messages.error(request, "Could not load subjects. Please try again later.")
    return render(request, 'frontend/subject_list.html', {'subjects': subjects})
