from itertools import chain


app_name = 'Accounts'

from .accounts_views.payment_views import payment_templates
from .accounts_views.bank_deposit_views import bank_deposit_templates
from .accounts_views.chart_of_account_views import chart_of_account_templates
from .accounts_views.debit_views import debit_templates
from .accounts_views.expense_views import expense_templates
from .accounts_views.journal_views import journal_templates
from .accounts_views.opening_views import opening_templates
from .accounts_views.receipt_views import receipt_templates


urlpatterns = list(chain(payment_templates,bank_deposit_templates,
                        chart_of_account_templates,debit_templates,expense_templates,
                        journal_templates,opening_templates,receipt_templates))
