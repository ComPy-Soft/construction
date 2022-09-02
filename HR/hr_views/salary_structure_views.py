from django.shortcuts import render
from django.urls import path


################################# Add & Manage Salary Structure ################################################
def add_salary_structure(request):
    return render(request, 'HR/Salary_Structures/add_salary_structure.html')

def manage_salary_structure(request):
    return render(request, 'HR/Salary_Structures/manage_salary_structure.html')

salary_structure_templates = [
    path('add_salary_structure/', add_salary_structure,name='add_salary_structure'),
    path('manage_salary_structure/', manage_salary_structure,name='manage_salary_structure'),
]