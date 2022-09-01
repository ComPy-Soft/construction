from django.shortcuts import render
from django.urls import path

def add_employee(request):
    return render(request, 'HR/Employees/add_employee.html')

def manage_employee(request):
    return render(request, 'HR/Employees/manage_employee.html')

employee_templates = [
    path('add_employee/', add_employee,name='add_employee'),
    path('manage_employee/', manage_employee,name='manage_employee'),
]