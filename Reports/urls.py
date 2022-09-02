from itertools import chain

from .report_views.accounts_views import accounts_templates
from .report_views.construction_views import construction_templates
from .report_views.inventory_views import inventory_templates
from .report_views.purchases_views import purchases_templates
from .report_views.sales_views import sales_templates

app_name = 'Reports'

urlpatterns = list(chain(
            accounts_templates,
            construction_templates,
            inventory_templates,
            purchases_templates,
            sales_templates
        ))