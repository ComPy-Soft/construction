from django.urls import path
from django.shortcuts import render

def add_installment_plan_B(request):
    return render(request, 'Sales/InstallmentPlanB/add_installment_plan_B.html')

def manage_installment_plan_B(request):
    return render(request, 'Sales/InstallmentPlanB/manage_installment_plan_B.html')

installment_plan_B_templates = [
    path('add_installment_plan_B/', add_installment_plan_B, name='add_installment_plan_B'),
    path('manage_installment_plan_B/', manage_installment_plan_B, name='manage_installment_plan_B'),
]