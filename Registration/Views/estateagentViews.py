from django.shortcuts import render
from django.urls import path
################################# Estate Agents Registration ################################################
def AddEstateAgents(request):
    return render(request, 'Registration/add_estate_agents.html')

def ManageEstateAgents(request):
    return render(request, 'Registration/manage_estate_agents.html')


estate_agent_template = [
    path('add_estate_agents/', AddEstateAgents, name='add_estate_agents'),
    path('manage_estate_agents/', ManageEstateAgents, name='manage_estate_agents'),
]