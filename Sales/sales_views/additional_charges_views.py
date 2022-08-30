from django.urls import path
from django.shortcuts import render


def add_additional_charges(request):
    return render(request, 'Sales/AdditionalCharges/add_additional_charges.html')

def manage_additional_charges(request):
    return render(request, 'Sales/AdditionalCharges/manage_additional_charges.html')


additional_charges_templates = [
    path('add_additional_charges/', add_additional_charges, name='add_additional_charges'),
    path('manage_additional_charges/', manage_additional_charges, name='manage_additional_charges'),
]