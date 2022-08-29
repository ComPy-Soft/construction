from django.shortcuts import render
from django.urls import path    

def AddReciept(request):
    return render(request, 'Accounts/add_receipt_voucher.html')

def ManageReceiept(request):
    return render(request, 'Accounts/manage_receipt_voucher.html')


receiept_templates = [
    path('add_receipt_voucher/', AddReciept,name='add_receipt_voucher'),
    path('manage_receipt_voucher', ManageReceiept,name='manage_receipt_voucher'),
    ]