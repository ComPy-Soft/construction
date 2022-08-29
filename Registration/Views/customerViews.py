from django.shortcuts import render
from django.urls import path


################################# Customer Registration ################################################

def AddCustomer(request):
    return render(request, 'Registration/add_customers.html')

def ManageCustomer(request):
    return render(request, 'Registration/manage_customers.html')


customer_template =[
    path('add_customers/', AddCustomer, name='add_customers'),
    path('manage_customers/', ManageCustomer, name='manage_customers'),
]