from django.shortcuts import render
from django.urls import path

def AddJournal(request):
    return render(request, 'Accounts/add_journal_voucher.html')

def ManageJournal(request):
    return render(request, 'Accounts/manage_journal_voucher.html')

journal_templates = [
    path('add_journal_voucher/', AddJournal,name='add_journal_voucher'),
    path('manage_journal_voucher', ManageJournal,name='manage_journal_voucher'),
    ]