from django.urls import path
from django.shortcuts import render

def add_property_transfer(request):
    return render(request, 'Sales/PropertyTransfer/add_property_transfer.html')

def manage_property_transfer(request):
    return render(request, 'Sales/PropertyTransfer/manage_property_transfer.html')

property_transfer_templates = [
    path('add_property_transfer/', add_property_transfer, name='add_property_transfer'),
    path('manage_property_transfer/', manage_property_transfer, name='manage_property_transfer'),
]