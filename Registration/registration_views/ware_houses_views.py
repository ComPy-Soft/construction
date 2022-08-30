from django.shortcuts import render
from django.urls import path

################################# Warehouses Registration ################################################
def add_ware_houses(request):
    return render(request, "Registration/add_warehouses.html")


def manage_ware_houses(request):
    return render(request, "Registration/manage_warehouses.html")


ware_houses_template = [
    path("add_warehouses/", add_ware_houses, name="add_warehouses"),
    path("manage_warehouses/", manage_ware_houses, name="manage_warehouses"),
]
