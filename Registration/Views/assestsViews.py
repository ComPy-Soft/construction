from django.shortcuts import render
from django.urls import path
################################ Assets Registration ################################################
def AddAssets(request):
    return render(request, 'Registration/add_assets.html')

def ManageAssets(request):
    return render(request, 'Registration/manage_assets.html')

assests_template = [
    path('add_assets/', AddAssets, name='add_assets'),
    path('manage_assets/', ManageAssets, name='manage_assets'),
]