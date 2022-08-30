from django.shortcuts import render
from django.urls import path

################################# Vendor Registration ################################################
def add_vendor(request):
    return render(request, "Registration/add_vendor.html")


def manage_vendor(request):
    return render(request, "Registration/manage_vendor.html")


vendor_template = [
    path("add_vendor/", add_vendor, name="add_vendor"),
    path("manage_vendor/", manage_vendor, name="manage_vendor"),
]
