from django.urls import path
from django.shortcuts import render

def add_property_surcharge(request):
    return render(request, 'Sales/PropertySurcharge/add_property_surcharge.html')

def manage_property_surcharge(request):
    return render(request, 'Sales/PropertySurcharge/manage_property_surcharge.html')

property_surcharge_templates = [
    path('add_property_surcharge/', add_property_surcharge, name='add_property_surcharge'),
    path('manage_property_surcharge/', manage_property_surcharge, name='manage_property_surcharge'),
]