from django.urls import path
from django.shortcuts import render

def add_installment_plan(request):
    return render(request, 'Sales/InstallmentPlanA/add_installment_plan.html')

def manage_installment_plan(request):
    return render(request, 'Sales/InstallmentPlanA/manage_installment_plan.html')

installment_plan_A_templates = [
    path('add_installment_plan/', add_installment_plan, name='add_installment_plan'),
    path('manage_installment_plan/', manage_installment_plan, name='manage_installment_plan'),
]