from django.shortcuts import render
from django.urls import path
################################# Product Types Registration ################################################
def AddProductTypes(request):
    return render(request, 'Registration/add_product_types.html')

def ManageProductTypes(request):
    return render(request, 'Registration/manage_product_types.html')


product_types_template = [


    path('add_product_types/', AddProductTypes, name='add_product_types'),
    path('manage_product_types/', ManageProductTypes, name='manage_product_types'),
]