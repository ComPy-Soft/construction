from django.urls import path
from django.shortcuts import render

def add_property_cancellation(request):
    return render(request, 'Sales/PropertyCancellation/add_property_cancellation.html')

def manage_property_cancellation(request):
    return render(request, 'Sales/PropertyCancellation/manage_property_cancellation.html')

property_cancellation_templates = [
    path('add_property_cancellation/', add_property_cancellation, name='add_property_cancellation'),
    path('manage_property_cancellation/', manage_property_cancellation, name='manage_property_cancellation'),
]