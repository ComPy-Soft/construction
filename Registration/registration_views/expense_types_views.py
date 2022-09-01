from django.shortcuts import render
from django.urls import path

################################# Expense Types Registration ################################################
def add_expense_types(request):
    return render(request, "Registration/Expense_Types/add_expense_types.html")


def manage_expense_types(request):
    return render(request, "Registration/Expense_Types/manage_expense_types.html")


expense_types_template = [
    path("add_expense_types/", add_expense_types, name="add_expense_types"),
    path("manage_expense_types/", manage_expense_types, name="manage_expense_types"),
]
