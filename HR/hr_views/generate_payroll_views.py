from django.shortcuts import render
from django.urls import path


################################# Generate Payroll ################################################
def generate_payroll(request):
    return render(request, 'HR/generate_pay_roll.html')

generate_payroll_templates = [
    path('generate_pay_roll/', generate_payroll,name='generate_pay_roll'),
]