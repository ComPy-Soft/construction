from django.shortcuts import render
from django.urls import path
################################# Estate Agents Registration ################################################
def add_estate_agent(request):
    return render(request, 'Registration/add_estate_agents.html')

def manage_estate_agent(request):
    return render(request, 'Registration/manage_estate_agents.html')


estate_agent_template = [
    path('add_estate_agents/', add_estate_agent, name='add_estate_agents'),
    path('manage_estate_agents/', manage_estate_agent, name='manage_estate_agents'),
]