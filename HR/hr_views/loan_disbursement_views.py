from django.shortcuts import render
from django.urls import path

def add_loan_disbursement(request):
    return render(request, 'HR/Loan_Disbursements/add_employee_loan_disbursement_voucher.html')

def manage_loan_disbursement(request):
    return render(request, 'HR/Loan_Disbursements/manage_loan_disbursement.html')


loan_disbursement_templates = [
    path('add_employee_loan_disbursement_voucher/', add_loan_disbursement,name='add_employee_loan_disbursement_voucher'),
    path('manage_loan_disbursement/', manage_loan_disbursement,name='manage_loan_disbursement'),
]