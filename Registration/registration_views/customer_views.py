from django.shortcuts import render
from django.urls import path


################################# Customer Registration ################################################

def add_customer(request):
    return render(request, 'Registration/add_customers.html')

def manage_customer(request):
    return render(request, 'Registration/manage_customers.html')


customer_template =[
    path('add_customers/', add_customer, name='add_customers'),
    path('manage_customers/', manage_customer, name='manage_customers'),
]