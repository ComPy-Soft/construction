"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (index,AddCustomer,ManageCustomer,AddVendor,ManageVendor,
                    AddEstateAgents,ManageEstateAgents,AddProductTypes,ManageProductTypes,
                    AddProducts,ManageProducts,AddTaxes,ManageTaxes,AddBankAccounts,ManageBankAccounts,
                    AddAssets,ManageAssets,AddUsers,ManageUsers,AddExpenseTypes,ManageExpenseTypes,
                    AddWarehouses,ManageWarehouses)
app_name = 'Registration'
urlpatterns = [
    path('', index, name='index'),
    path('add_customers/', AddCustomer, name='add_customers'),
    path('manage_customers/', ManageCustomer, name='manage_customers'),


    path('add_vendor/', AddVendor, name='add_vendor'),
    path('manage_vendor/', ManageVendor, name='manage_vendor'),



    path('add_estate_agents/', AddEstateAgents, name='add_estate_agents'),
    path('manage_estate_agents/', ManageEstateAgents, name='manage_estate_agents'),

    path('add_product_types/', AddProductTypes, name='add_product_types'),
    path('manage_product_types/', ManageProductTypes, name='manage_product_types'),


    path('add_products/', AddProducts, name='add_products'),
    path('manage_products/', ManageProducts, name='manage_products'),


    path('add_taxes/', AddTaxes, name='add_taxes'),
    path('manage_taxes/', ManageTaxes, name='manage_taxes'),


    path('add_bank_accounts/', AddBankAccounts, name='add_bank_accounts'),
    path('manage_bank_accounts/', ManageBankAccounts, name='manage_bank_accounts'),


    path('add_assets/', AddAssets, name='add_assets'),
    path('manage_assets/', ManageAssets, name='manage_assets'),


    path('add_users/', AddUsers, name='add_users'),
    path('manage_users/', ManageUsers, name='manage_users'),


    path('add_expense_types/', AddExpenseTypes, name='add_expense_types'),
    path('manage_expense_types/', ManageExpenseTypes, name='manage_expense_types'),


    path('add_warehouses/', AddWarehouses, name='add_warehouses'),
    path('manage_warehouses/', ManageWarehouses, name='manage_warehouses'),


    
]
