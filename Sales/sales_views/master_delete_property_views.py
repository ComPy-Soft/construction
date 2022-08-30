from django.urls import path
from django.shortcuts import render

def master_delete_property_sales(request):
    return render(request, 'Sales/master_delete_property_sales.html')


master_delete_property_templates = [
    path('master_delete_property_sales/', master_delete_property_sales, name='master_delete_property_sales'),
]