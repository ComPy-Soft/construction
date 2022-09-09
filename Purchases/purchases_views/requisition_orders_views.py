from django.urls import path
from django.shortcuts import render

def add_requisition_order(request):
    return render(request, 'Purchases/Requisition_Orders/add_requisition_order.html')

def manage_requisition_order(request):
    return render(request, 'Purchases/Requisition_Orders/manage_requisition_order.html')

requisition_order_template = [
    path('add_requisition_order/', add_requisition_order, name='add_requisition_order'),
    path('manage_requisition_order/', manage_requisition_order, name='manage_requisition_order'),
]