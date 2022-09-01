from django.shortcuts import render
from django.urls import path
################################# Products Registration ################################################
def add_product(request):
    return render(request, 'Registration/Products/add_products.html')

def manage_product(request):
    return render(request, 'Registration/Products/manage_products.html')

product_template = [
    path('add_products/', add_product, name='add_products'),
    path('manage_products/', manage_product, name='manage_products'),
]