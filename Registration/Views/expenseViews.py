from django.shortcuts import render
from django.urls import path

################################# Expense Types Registration ################################################
def AddExpenseTypes(request):
    return render(request, "Registration/add_expense_types.html")


def ManageExpenseTypes(request):
    return render(request, "Registration/manage_expense_types.html")


expense_types_template = [
    path("add_expense_types/", AddExpenseTypes, name="add_expense_types"),
    path("manage_expense_types/", ManageExpenseTypes, name="manage_expense_types"),
]
