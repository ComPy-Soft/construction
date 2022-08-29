from django.shortcuts import render
from django.urls import path

################################# Vendor Registration ################################################
def AddVendor(request):
    return render(request, "Registration/add_vendor.html")


def ManageVendor(request):
    return render(request, "Registration/manage_vendor.html")


vendor_template = [
    path("add_vendor/", AddVendor, name="add_vendor"),
    path("manage_vendor/", ManageVendor, name="manage_vendor"),
]
