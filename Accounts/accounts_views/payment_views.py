from django.shortcuts import render
from django.urls import path

def add_payment(request):
    return render(request, 'Accounts/add_payment_voucher.html')

def manage_payment(request):
    return render(request, 'Accounts/manage_payment_voucher.html')


payment_templates = [
    path('add_payment_voucher/', add_payment,name='add_payment_voucher'),
    path('manage_payment_voucher', manage_payment,name='manage_payment_voucher'),
    ]