
from django.urls import path
from itertools import chain
from .registration_views.assests_views import assests_template
from .registration_views.taxes_views import taxes_template
from .registration_views.users_views import users_template
from .registration_views.index_views import index_template
from .registration_views.customer_views import customer_template
from .registration_views.estate_agent_views import estate_agent_template
from .registration_views.expense_types_views import expense_types_template
from .registration_views.product_types_views import product_types_template
from .registration_views.product_views import product_template
from .registration_views.vendor_views import vendor_template
from .registration_views.ware_houses_views import ware_houses_template
from .registration_views.bank_account_views import bank_account_template


app_name = 'Registration'

urlpatterns = list(chain(assests_template, taxes_template,
                        users_template, index_template, customer_template,
                        estate_agent_template, expense_types_template,
                        product_types_template, product_template,
                        vendor_template, ware_houses_template, bank_account_template))
