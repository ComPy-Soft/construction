from django.shortcuts import render
from django.urls import path

def add_debit(request):
    return render(request, 'Accounts/add_debit_notes.html')

def manage_debit(request):
    return render(request, 'Accounts/manage_debit_notes.html')

debit_templates = [
    path('add_debit_notes/', add_debit,name='add_debit_notes'),
    path('manage_debit_notes', manage_debit,name='manage_debit_notes'),
    ]