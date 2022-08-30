
from django.shortcuts import render
from django.urls import path


def chart_of_account(request):
    return render(request, 'Accounts/chart_of_accounts.html')

chart_of_account_templates = [
    path('chart_of_accounts/', chart_of_account,name='chart_of_accounts'),
    ]