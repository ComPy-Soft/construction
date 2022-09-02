from django.shortcuts import render
from django.urls import path

################################# Add Construction Ledgers ################################################

def construction_ledger(request):
    return render(request, 'Reports/Construction/construction_ledger.html')

def delayed_construction_stages(request):
    return render(request, 'Reports/Construction/delayed_construction_stages.html')


construction_templates = [
    path('construction_ledger/', construction_ledger,name='construction_ledger'),
    path('delayed_construction_stages/', delayed_construction_stages,name='delayed_construction_stages'),
]