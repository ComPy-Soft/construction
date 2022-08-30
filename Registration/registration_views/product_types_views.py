from django.shortcuts import render
from django.urls import path
################################# Product Types Registration ################################################
def add_product_types(request):
    return render(request, 'Registration/add_product_types.html')

def manage_product_types(request):
    return render(request, 'Registration/manage_product_types.html')


product_types_template = [


    path('add_product_types/', add_product_types, name='add_product_types'),
    path('manage_product_types/', manage_product_types, name='manage_product_types'),
]