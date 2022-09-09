from django.urls import path
from django.shortcuts import render

def add_stock_receiving_voucher(request):
    return render(request, 'Purchases/Stock_Vouchers/add_stock_receiving_voucher.html')

def manage_stock_voucher(request):
    return render(request, 'Purchases/Stock_Vouchers/manage_stock_voucher.html')

stock_voucher_template = [
    path('add_stock_receiving_voucher/', add_stock_receiving_voucher, name='add_stock_receiving_voucher'),
    path('manage_stock_voucher/', manage_stock_voucher, name='manage_stock_voucher'),
]