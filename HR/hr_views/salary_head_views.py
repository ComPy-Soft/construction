from django.shortcuts import render
from django.urls import path


def add_salary_head(request):
    return render(request, 'HR/Salary_Heads/add_salary_head.html')

def manage_salary_head(request):
    return render(request, 'HR/Salary_Heads/manage_salary_head.html')

salary_head_templates = [
    path('add_salary_head/', add_salary_head,name='add_salary_head'),
    path('manage_salary_head/', manage_salary_head,name='manage_salary_head'),
]