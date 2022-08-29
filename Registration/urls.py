from .Views.indexViews import index
from django.urls import path
from itertools import chain
from .Views.customerViews import customer_template
from .Views.vendorViews import vendor_template
from .Views.assestsViews import assests_template
from .Views.bankAccountViews import bank_accounts_template
from .Views.estateagentViews import estate_agent_template
from .Views.wareHousesViews import warehouses_template
from .Views.productTypesViews import product_types_template
from .Views.productViews import product_template
from .Views.usersViews import users_template
from .Views.expenseViews import expense_types_template
from .Views.taxesViews import taxes_template

app_name = 'Registration'

urlpatterns = list(chain([
    path('', index, name='index'),
],customer_template, vendor_template, assests_template,
bank_accounts_template, estate_agent_template, warehouses_template,
product_types_template, product_template, users_template, expense_types_template, taxes_template))
