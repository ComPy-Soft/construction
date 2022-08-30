from django.shortcuts import render
from django.urls import path

def add_bank_deposit(request):
    return render(request, 'Accounts/add_bank_deposit_voucher.html')

def manage_bank_deposit(request):
    return render(request, 'Accounts/manage_bank_deposit_voucher.html')

bank_deposit_templates = [
    path('add_bank_deposit_voucher/', add_bank_deposit,name='add_bank_deposit_voucher'),
    path('manage_bank_deposit_voucher/', manage_bank_deposit,name='manage_bank_deposit_voucher'),
    ]