from django.shortcuts import render
from django.urls import path

################################# Bank Accounts Registration ################################################
def add_bank_account(request):
    return render(request, "Registration/Bank_Accounts/add_bank_accounts.html")


def manage_bank_account(request):
    return render(request, "Registration/Bank_Accounts/manage_bank_accounts.html")


bank_account_template = [
    path("add_bank_accounts/", add_bank_account, name="add_bank_accounts"),
    path("manage_bank_accounts/", manage_bank_account, name="manage_bank_accounts"),
]
