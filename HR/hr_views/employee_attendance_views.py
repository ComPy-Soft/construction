from django.shortcuts import render
from django.urls import path

def add_employee_attendance(request):
    return render(request, 'HR/Employee_Attendance/add_employee_attendance.html')

def manage_employee_attendance(request):
    return render(request, 'HR/Employee_Attendance/manage_employee_attendance.html')

employee_attendance_templates = [
    path('add_employee_attendance/', add_employee_attendance,name='add_employee_attendance'),
    path('manage_employee_attendance/', manage_employee_attendance,name='manage_employee_attendance'),
]