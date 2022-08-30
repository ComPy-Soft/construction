from django.shortcuts import render
from django.urls import path

def manage_properties(request):
    return render(request, 'Sales/properties/manage_properties.html')

def generate_properties(request):
    return render(request, 'Sales/properties/generate_properties.html')


properties_templates = [
    path('manage_properties/', manage_properties, name='manage_properties'),
    path('generate_properties/', generate_properties, name='generate_properties'),
]