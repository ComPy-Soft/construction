from django.urls import path 
from django.shortcuts import render

def add_agent_commission(request):
    return render(request, 'Sales/AgentCommission/add_agent_commission.html')

def manage_agent_commission(request):
    return render(request, 'Sales/AgentCommission/manage_agent_commission.html')

agent_commission_templates = [
    path('add_agent_commission/', add_agent_commission, name='add_agent_commission'),
    path('manage_agent_commission/', manage_agent_commission, name='manage_agent_commission'),
]