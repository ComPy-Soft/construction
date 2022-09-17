from django.urls import path
from django.shortcuts import render

def add_requisition_approval(request):
    return render(request, 'Purchases/Requisition_Approvals/add_requisition_approval.html')

def manage_requisition_approval(request):
    return render(request, 'Purchases/Requisition_Approvals/manage_requisition_approval.html')

requisition_approval_template = [
    path('add_requisition_approval/', add_requisition_approval, name='add_requisition_approval'),
    path('manage_requisition_approval/', manage_requisition_approval, name='manage_requisition_approval'),
]