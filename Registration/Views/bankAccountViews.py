from django.shortcuts import render
from django.urls import path

################################# Bank Accounts Registration ################################################
def AddBankAccounts(request):
    return render(request, "Registration/add_bank_accounts.html")


def ManageBankAccounts(request):
    return render(request, "Registration/manage_bank_accounts.html")


bank_accounts_template = [
    path("add_bank_accounts/", AddBankAccounts, name="add_bank_accounts"),
    path("manage_bank_accounts/", ManageBankAccounts, name="manage_bank_accounts"),
]
