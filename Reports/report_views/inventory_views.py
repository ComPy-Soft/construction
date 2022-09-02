from django.shortcuts import render
from django.urls import path


################################# Add Inventory Ledgers ################################################

def breakage_report(request):
    return render(request, 'Reports/Inventory/breakage_report.html')


def inventory_consumed_value_wise(request):
    return render(request, 'Reports/Inventory/inventory_consumed_value_wise.html')


def inventory_consumption(request):
    return render(request, 'Reports/Inventory/inventory_consumption.html')


def inventory_in_hand(request):
    return render(request, 'Reports/Inventory/inventory_in_hand.html')


def inventory_ledger(request):
    return render(request, 'Reports/Inventory/inventory_ledger.html')


def inventory_procured_value_wise(request):
    return render(request, 'Reports/Inventory/inventory_procured_value_wise.html')


def inventory_report(request):
    return render(request, 'Reports/Inventory/inventory_report.html')


def inventory_value_wise(request):
    return render(request, 'Reports/Inventory/inventory_value_wise.html')


inventory_templates = [
    path('breakage_report/', breakage_report, name='breakage_report'),
    path('inventory_consumed_value_wise/', inventory_consumed_value_wise, name='inventory_consumed_value_wise'),
    path('inventory_consumption/', inventory_consumption, name='inventory_consumption'),
    path('inventory_in_hand/', inventory_in_hand, name='inventory_in_hand'),
    path('inventory_ledger/', inventory_ledger, name='inventory_ledger'),
    path('inventory_procured_value_wise/', inventory_procured_value_wise, name='inventory_procured_value_wise'),
    path('inventory_report/', inventory_report, name='inventory_report'),
    path('inventory_value_wise/', inventory_value_wise, name='inventory_value_wise'),
]

