from django.shortcuts import render
from django.urls import path

def AddOpening(request):
    return render(request, 'Accounts/add_opening_voucher.html')

def ManageOpening(request):
    return render(request, 'Accounts/manage_opening_voucher.html')

opening_templates = [
    path('add_opening_voucher/', AddOpening,name='add_opening_voucher'),
    path('manage_opening_voucher', ManageOpening,name='manage_opening_voucher'),
    ]