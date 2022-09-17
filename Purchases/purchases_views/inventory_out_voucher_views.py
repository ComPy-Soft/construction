from django.urls import path
from django.shortcuts import render

def add_inventory_out_voucher(request):
    return render(request, 'Purchases/Inventory_Out_Vouchers/add_inventory_out_voucher.html')

def manage_inventory_out_voucher(request):
    return render(request, 'Purchases/Inventory_Out_Vouchers/manage_inventory_out_voucher.html')

inventory_out_voucher_template = [
    path('add_inventory_out_voucher/', add_inventory_out_voucher, name='add_inventory_out_voucher'),
    path('manage_inventory_out_voucher/', manage_inventory_out_voucher, name='manage_inventory_out_voucher'),   
]