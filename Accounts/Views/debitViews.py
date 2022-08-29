from django.shortcuts import render
from django.urls import path

def AddDebit(request):
    return render(request, 'Accounts/add_debit_notes.html')

def ManageDebit(request):
    return render(request, 'Accounts/manage_debit_notes.html')

debit_templates = [
    path('add_debit_notes/', AddDebit,name='add_debit_notes'),
    path('manage_debit_notes', ManageDebit,name='manage_debit_notes'),
    ]