from django.shortcuts import render
from django.urls import path

def AddBankDeposit(request):
    return render(request, 'Accounts/add_bank_deposit_voucher.html')

def ManageBankDeposit(request):
    return render(request, 'Accounts/manage_bank_deposit_voucher.html')

bank_deposit_templates = [
    path('add_bank_deposit_voucher/', AddBankDeposit,name='add_bank_deposit_voucher'),
    path('manage_bank_deposit_voucher/', ManageBankDeposit,name='manage_bank_deposit_voucher'),
    ]