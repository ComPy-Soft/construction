from django.urls import path
from django.shortcuts import render

def add_property_buy_back(request):
    return render(request, 'Sales/BuyBack/add_property_buy_back.html')

def manage_property_buy_back(request):
    return render(request, 'Sales/BuyBack/manage_property_buy_back.html')

buy_back_templates = [
    path('add_property_buy_back/', add_property_buy_back, name='add_property_buy_back'),
    path('manage_property_buy_back/', manage_property_buy_back, name='manage_property_buy_back'),
]