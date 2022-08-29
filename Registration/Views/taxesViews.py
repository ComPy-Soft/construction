from django.shortcuts import render
from django.urls import path
################################# Taxes Registration ################################################
def AddTaxes(request):
    return render(request, "Registration/add_taxes.html")


def ManageTaxes(request):
    return render(request, "Registration/manage_taxes.html")


taxes_template = [
    path("add_taxes/", AddTaxes, name="add_taxes"),
    path("manage_taxes/", ManageTaxes, name="manage_taxes"),
]
