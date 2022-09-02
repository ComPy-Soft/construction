from django.shortcuts import render
from django.urls import path

################################# Add Purchases Ledgers ################################################

def batch_analysis_report(request):
    return render(request, 'Reports/Purchases/batch_analysis_report.html')


def pending_requisition_orders(request):
    return render(request, 'Reports/Purchases/pending_requisition_orders.html')

def pending_stock_for_purch_order(request):
    return render(request, 'Reports/Purchases/pending_stock_for_purch_order.html')

def previous_requisition_actions(request):
    return render(request, 'Reports/Purchases/previous_requisition_actions.html')

def product_wise_purchase(request):
    return render(request, 'Reports/Purchases/product_wise_purchase.html')

def requisition_order_status(request):
    return render(request, 'Reports/Purchases/requisition_order_status.html')

def vendor_wise_purchase(request):
    return render(request, 'Reports/Purchases/vendor_wise_purchase.html')


purchases_templates = [
    path('batch_analysis_report/', batch_analysis_report, name='batch_analysis_report'),
    path('pending_requisition_orders/', pending_requisition_orders, name='pending_requisition_orders'),
    path('pending_stock_for_purch_order/', pending_stock_for_purch_order, name='pending_stock_for_purch_order'),
    path('previous_requisition_actions/', previous_requisition_actions, name='previous_requisition_actions'),
    path('product_wise_purchase/', product_wise_purchase, name='product_wise_purchase'),
    path('requisition_order_status/', requisition_order_status, name='requisition_order_status'),
    path('vendor_wise_purchase/', vendor_wise_purchase, name='vendor_wise_purchase'),
]