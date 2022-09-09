from django.urls import path
from django.shortcuts import render

def add_purchase_order(request):
    return render(request, 'Purchases/Purchase_Orders/add_purchase_order.html')

def manage_purchase_orders(request):
    return render(request, 'Purchases/Purchase_Orders/manage_purchase_orders.html')

purchase_order_template = [
    path('add_purchase_order/', add_purchase_order, name='add_purchase_order'),
    path('manage_purchase_orders/', manage_purchase_orders, name='manage_purchase_orders'),
]