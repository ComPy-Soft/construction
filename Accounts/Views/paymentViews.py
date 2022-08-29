from django.shortcuts import render
from django.urls import path

def AddPayment(request):
    return render(request, 'Accounts/add_payment_voucher.html')

def ManagePayment(request):
    return render(request, 'Accounts/manage_payment_voucher.html')


payment_templates = [
    path('add_payment_voucher/', AddPayment,name='add_payment_voucher'),
    path('manage_payment_voucher', ManagePayment,name='manage_payment_voucher'),
    ]