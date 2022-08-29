from django.urls import path
from django.shortcuts import render

def AddExpense(request):
    return render(request, 'Accounts/add_expense_voucher.html')

def ManageExpense(request):
    return render(request, 'Accounts/manage_expense_voucher.html')  

expense_templates = [
    path('add_expense_voucher/', AddExpense,name='add_expense_voucher'),
    path('manage_expense_voucher', ManageExpense,name='manage_expense_voucher'),
    ]