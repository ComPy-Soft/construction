from django.urls import path
from django.shortcuts import render

def add_property_sale(request):
    return render(request, 'Sales/PropertySale/add_property_sale.html')

def manage_property_sale(request):
    return render(request, 'Sales/PropertySale/manage_property_sale.html')

property_sale_templates = [
    path('add_property_sale/', add_property_sale, name='add_property_sale'),
    path('manage_property_sale/', manage_property_sale, name='manage_property_sale'),
]