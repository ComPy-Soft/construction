from django.urls import path
from django.shortcuts import render

def add_surcharge_waiver(request):
    return render(request, 'Sales/SurchargeWaiver/add_surcharge_waiver.html')

def manage_surcharge_waiver(request):
    return render(request, 'Sales/SurchargeWaiver/manage_surcharge_waiver.html')

surcharge_waiver_templates = [
    path('add_surcharge_waiver/', add_surcharge_waiver, name='add_surcharge_waiver'),
    path('manage_surcharge_waiver/', manage_surcharge_waiver, name='manage_surcharge_waiver'),
]