from django.shortcuts import render
from django.urls import path    

def add_receipt(request):
    return render(request, 'Accounts/Receipt_Vouchers/add_receipt_voucher.html')

def manage_receipt(request):
    return render(request, 'Accounts/Receipt_Vouchers/manage_receipt_voucher.html')


receipt_templates = [
    path('add_receipt_voucher/', add_receipt,name='add_receipt_voucher'),
    path('manage_receipt_voucher', manage_receipt,name='manage_receipt_voucher'),
    ]