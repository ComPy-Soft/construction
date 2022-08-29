from django.shortcuts import render
from django.urls import path

################################# Warehouses Registration ################################################
def AddWarehouses(request):
    return render(request, "Registration/add_warehouses.html")


def ManageWarehouses(request):
    return render(request, "Registration/manage_warehouses.html")


warehouses_template = [
    path("add_warehouses/", AddWarehouses, name="add_warehouses"),
    path("manage_warehouses/", ManageWarehouses, name="manage_warehouses"),
]
