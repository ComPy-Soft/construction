from django.shortcuts import render
from django.urls import path


################################# Add & Manage Loan Receipt ################################################
def add_loan_receipt(request):
    return render(request, 'HR/Loan_Receipts/add_employee_loan_payment_receipt.html')

def manage_loan_receipt(request):
    return render(request, 'HR/Loan_Receipts/manage_loan_receipt.html')

loan_receipts_templates = [
    path('add_employee_loan_payment_receipt/', add_loan_receipt,name='add_employee_loan_payment_receipt'),
    path('manage_loan_receipt/', manage_loan_receipt,name='manage_loan_receipt'),
]