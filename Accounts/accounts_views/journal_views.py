from django.shortcuts import render
from django.urls import path

def add_journal(request):
    return render(request, 'Accounts/add_journal_voucher.html')

def manage_journal(request):
    return render(request, 'Accounts/manage_journal_voucher.html')

journal_templates = [
    path('add_journal_voucher/', add_journal,name='add_journal_voucher'),
    path('manage_journal_voucher', manage_journal,name='manage_journal_voucher'),
    ]