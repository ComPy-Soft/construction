from itertools import chain


app_name = 'Accounts'

from .Views.paymentViews import payment_templates
from .Views.bankDepositViews import bank_deposit_templates
from .Views.chartAccountViews import chart_accounts_templates
from .Views.debitViews import debit_templates
from .Views.expenseViews import expense_templates
from .Views.journelViews import journal_templates
from .Views.openingViews import opening_templates
from .Views.receiptViews import receiept_templates


urlpatterns = list(chain(payment_templates,bank_deposit_templates,
chart_accounts_templates,debit_templates,expense_templates,
journal_templates,opening_templates,receiept_templates))
