from django.shortcuts import render
from django.urls import path
################################# Taxes Registration ################################################
def add_taxes(request):
    return render(request, "Registration/Taxes/add_taxes.html")


def manage_taxes(request):
    return render(request, "Registration/Taxes/manage_taxes.html")


taxes_template = [
    path("add_taxes/", add_taxes, name="add_taxes"),
    path("manage_taxes/", manage_taxes, name="manage_taxes"),
]
