from django.shortcuts import render
from django.urls import path
################################# Products Registration ################################################
def AddProducts(request):
    return render(request, 'Registration/add_products.html')

def ManageProducts(request):
    return render(request, 'Registration/manage_products.html')

product_template = [
    path('add_products/', AddProducts, name='add_products'),
    path('manage_products/', ManageProducts, name='manage_products'),
]