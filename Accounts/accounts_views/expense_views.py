from django.urls import path
from django.shortcuts import render

def add_expense(request):
    return render(request, 'Accounts/add_expense_voucher.html')

def manage_expense(request):
    return render(request, 'Accounts/manage_expense_voucher.html')  

expense_templates = [
    path('add_expense_voucher/', add_expense,name='add_expense_voucher'),
    path('manage_expense_voucher', manage_expense,name='manage_expense_voucher'),
    ]