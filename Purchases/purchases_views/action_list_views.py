from django.urls import path
from django.shortcuts import render

def requisition_approval_action_list(request):
    return render(request, 'Purchases/requisition_approval_action_list.html')

action_list_template = [path('requisition_approval_action_list/', requisition_approval_action_list, name='requisition_approval_action_list')]