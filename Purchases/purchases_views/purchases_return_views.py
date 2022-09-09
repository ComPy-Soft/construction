from django.urls import path
from django.shortcuts import render

def add_purchase_return(request):
    return render(request, 'Purchases/Purchase_Returns/add_purchase_return.html')

def manage_purchase_return(request):
    return render(request, 'Purchases/Purchase_Returns/manage_purchase_returns.html')

purchase_return_template = [
    path('add_purchase_return/', add_purchase_return, name='add_purchase_return'),
    path('manage_purchase_returns/', manage_purchase_return, name='manage_purchase_returns'),
]