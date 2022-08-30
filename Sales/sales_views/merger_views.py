from django.urls import path
from django.shortcuts import render

def add_property_merger(request):
    return render(request, 'Sales/PropertyMerger/add_property_merger.html')

def manage_property_merger(request):
    return render(request, 'Sales/PropertyMerger/manage_property_merger.html')

property_merger_templates = [
    path('add_property_merger/', add_property_merger, name='add_property_merger'),
    path('manage_property_merger/', manage_property_merger, name='manage_property_merger'),
]