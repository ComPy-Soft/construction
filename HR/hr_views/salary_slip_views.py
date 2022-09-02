from django.shortcuts import render
from django.urls import path


################################# Add & Manage Salary Slip ################################################
def add_salary_slip(request):
    return render(request, 'HR/Salary_Slips/add_salary_slip.html')

def manage_salary_slip(request):
    return render(request, 'HR/Salary_Slips/manage_salary_slips.html')

salary_slip_templates = [
    path('add_salary_slip/', add_salary_slip,name='add_salary_slip'),
    path('manage_salary_slips/', manage_salary_slip,name='manage_salary_slips'),
]