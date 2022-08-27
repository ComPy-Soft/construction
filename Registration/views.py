from django.shortcuts import render





# Create your views here.
def index(request):
    return render(request, 'Registration/index.html')




################################# Customer Registration ################################################

def AddCustomer(request):
    return render(request, 'Registration/add_customers.html')

def ManageCustomer(request):
    return render(request, 'Registration/manage_customers.html')



################################# Vendor Registration ################################################
def AddVendor(request):
    return render(request, 'Registration/add_vendor.html')

def ManageVendor(request):
    return render(request, 'Registration/manage_vendor.html')


################################# Estate Agents Registration ################################################
def AddEstateAgents(request):
    return render(request, 'Registration/add_estate_agents.html')

def ManageEstateAgents(request):
    return render(request, 'Registration/manage_estate_agents.html')


################################# Product Types Registration ################################################
def AddProductTypes(request):
    return render(request, 'Registration/add_product_types.html')

def ManageProductTypes(request):
    return render(request, 'Registration/manage_product_types.html')



################################# Products Registration ################################################
def AddProducts(request):
    return render(request, 'Registration/add_products.html')

def ManageProducts(request):
    return render(request, 'Registration/manage_products.html')


################################# Taxes Registration ################################################
def AddTaxes(request):
    return render(request, 'Registration/add_taxes.html')

def ManageTaxes(request):
    return render(request, 'Registration/manage_taxes.html')


################################# Bank Accounts Registration ################################################
def AddBankAccounts(request):
    return render(request, 'Registration/add_bank_accounts.html')

def ManageBankAccounts(request):
    return render(request, 'Registration/manage_bank_accounts.html')


################################# Assets Registration ################################################
def AddAssets(request):
    return render(request, 'Registration/add_assets.html')

def ManageAssets(request):
    return render(request, 'Registration/manage_assets.html')


################################# Users Registration ################################################
def AddUsers(request):
    return render(request, 'Registration/add_users.html')

def ManageUsers(request):
    return render(request, 'Registration/manage_users.html')


################################# Expense Types Registration ################################################
def AddExpenseTypes(request):
    return render(request, 'Registration/add_expense_types.html')

def ManageExpenseTypes(request):
    return render(request, 'Registration/manage_expense_types.html')


################################# Warehouses Registration ################################################
def AddWarehouses(request):
    return render(request, 'Registration/add_warehouses.html')

def ManageWarehouses(request):
    return render(request, 'Registration/manage_warehouses.html')
    