from django.shortcuts import render
from django.urls import path


################################# Add Reports with ledgers ################################################

def account_ledger(request):
    return render(request, 'Reports/Accounts/account_ledger.html')

def account_payables(request):
    return render(request, 'Reports/Accounts/account_payables.html')

def account_receivables(request):
    return render(request, 'Reports/Accounts/account_receivables.html')

def balance_sheet(request):
    return render(request, 'Reports/Accounts/balance_sheet.html')

def balance_sheet_summary(request):
    return render(request, 'Reports/Accounts/balance_sheet_summary.html')

def bank_ledger(request):
    return render(request, 'Reports/Accounts/bank_ledger.html')

def customer_ledger(request):
    return render(request, 'Reports/Accounts/customer_ledger.html')

def employee_commission_ledger(request):
    return render(request, 'Reports/Accounts/employee_commission_ledger.html')

def employee_ledger(request):
    return render(request, 'Reports/Accounts/employee_ledger.html')

def estate_agent_ledger(request):
    return render(request, 'Reports/Accounts/estate_agent_ledger.html')

def general_ledger(request):
    return render(request, 'Reports/Accounts/general_ledger.html')

def profit_loss_statement(request):
    return render(request, 'Reports/Accounts/profit_loss_statement.html')

def trial_balance(request):
    return render(request, 'Reports/Accounts/trial_balance.html')

def vendor_ledger(request):
    return render(request, 'Reports/Accounts/vendor_ledger.html')

accounts_templates = [
    path('account_ledger/', account_ledger,name='account_ledger'),
    path('account_payables/', account_payables,name='account_payables'),
    path('account_receivables/', account_receivables,name='account_receivables'),
    path('balance_sheet/', balance_sheet,name='balance_sheet'),
    path('balance_sheet_summary/', balance_sheet_summary,name='balance_sheet_summary'),
    path('bank_ledger/', bank_ledger,name='bank_ledger'),
    path('customer_ledger/', customer_ledger,name='customer_ledger'),
    path('employee_commission_ledger/', employee_commission_ledger,name='employee_commission_ledger'),
    path('employee_ledger/', employee_ledger,name='employee_ledger'),
    path('estate_agent_ledger/', estate_agent_ledger,name='estate_agent_ledger'),
    path('general_ledger/', general_ledger,name='general_ledger'),
    path('profit_loss_statement/', profit_loss_statement,name='profit_loss_statement'),
    path('trial_balance/', trial_balance,name='trial_balance'),
    path('vendor_ledger/', vendor_ledger,name='vendor_ledger'),
]
