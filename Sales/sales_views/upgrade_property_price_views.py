from django.urls import path
from django.shortcuts import render

def upgrade_property_prices(request):
    return render(request, 'Sales/upgrade_property_prices.html')

upgrade_property_prices_templates = [
    path('upgrade_property_prices/', upgrade_property_prices, name='upgrade_property_prices'),
]