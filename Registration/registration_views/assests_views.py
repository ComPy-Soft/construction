from django.shortcuts import render
from django.urls import path
################################ Assets Registration ################################################
def add_assests(request):
    return render(request, 'Registration/Assets/add_assets.html')

def manage_assests(request):
    return render(request, 'Registration/Assets/manage_assets.html')

assests_template = [
    path('add_assets/',add_assests, name='add_assets'),
    path('manage_assets/', manage_assests, name='manage_assets'),
]

