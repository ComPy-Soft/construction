from django.shortcuts import render
from django.urls import path

################################# Add Sales Ledgers ################################################

def customer_properties_summary(request):
    return render(request, 'Reports/Sales/customer_properties_summary.html')

def due_installments(request):
    return render(request, 'Reports/Sales/due_installments.html')


def late_installments(request):
    return render(request, 'Reports/Sales/late_installments.html')

def outstanding_additional_charges(request):
    return render(request, 'Reports/Sales/outstanding_additional_charges.html')

def outstanding_installments(request):
    return render(request, 'Reports/Sales/outstanding_installments.html')

def payment_collection(request):
    return render(request, 'Reports/Sales/payment_collection.html')

def property_wise_due(request):
    return render(request, 'Reports/Sales/property_wise_due.html')

def property_wise_outstandings(request):
    return render(request, 'Reports/Sales/property_wise_outstandings.html')

def sales_property_statement(request):
    return render(request, 'Reports/Sales/sales_property_statement.html')

def sales_with_full_payment(request):
    return render(request, 'Reports/Sales/sales_with_full_payment.html')


sales_templates = [
    path('customer_properties_summary/', customer_properties_summary, name='customer_properties_summary'),
    path('due_installments/', due_installments, name='due_installments'),
    path('late_installments/', late_installments, name='late_installments'),
    path('outstanding_additional_charges/', outstanding_additional_charges, name='outstanding_additional_charges'),
    path('outstanding_installments/', outstanding_installments, name='outstanding_installments'),
    path('payment_collection/', payment_collection, name='payment_collection'),
    path('property_wise_due/', property_wise_due, name='property_wise_due'),
    path('property_wise_outstandings/', property_wise_outstandings, name='property_wise_outstandings'),
    path('sales_property_statement/', sales_property_statement, name='sales_property_statement'),
    path('sales_with_full_payment/', sales_with_full_payment, name='sales_with_full_payment'),
]