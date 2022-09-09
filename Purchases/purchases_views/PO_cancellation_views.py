from django.urls import path
from django.shortcuts import render

def add_purchase_order_cancel(request):
    return render(request, 'Purchases/PO_Cancellation/add_purchase_order_cancel.html')

def manage_purchase_order_cancel(request):
    return render(request, 'Purchases/PO_Cancellation/manage_purchase_order_cancel.html')

purchase_order_cancel_template = [
    path('add_purchase_order_cancel/', add_purchase_order_cancel, name='add_purchase_order_cancel'),
    path('manage_purchase_order_cancel/', manage_purchase_order_cancel, name='manage_purchase_order_cancel'),
]