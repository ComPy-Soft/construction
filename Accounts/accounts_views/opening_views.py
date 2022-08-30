from django.shortcuts import render
from django.urls import path

def add_opening(request):
    return render(request, 'Accounts/add_opening_voucher.html')

def manage_opening(request):
    return render(request, 'Accounts/manage_opening_voucher.html')

opening_templates = [
    path('add_opening_voucher/', add_opening,name='add_opening_voucher'),
    path('manage_opening_voucher/', manage_opening,name='manage_opening_voucher'),
    ]