from django.shortcuts import render





# Create your views here.
def index(request):
    return render(request, 'Registration/index.html')




################################# Customer Registration ################################################

def AddCustomer(request):
    return render(request, 'Registration/add_customers.html')

def ManageCustomer(request):
    return render(request, 'Registration/manage_customers.html')



################################# Vendor Registration ################################################
def AddVendor(request):
    return render(request, 'Registration/add_vendor.html')

def ManageVendor(request):
    return render(request, 'Registration/manage_vendor.html')