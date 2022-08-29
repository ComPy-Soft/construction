
from django.shortcuts import render
from django.urls import path


def ChartOfAccounts(request):
    return render(request, 'Accounts/chart_of_accounts.html')

chart_accounts_templates = [
    path('chart_of_accounts/', ChartOfAccounts,name='chart_of_accounts'),
    ]