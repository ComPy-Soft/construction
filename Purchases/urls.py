from itertools import chain

app_name = 'Purchases'

from .purchases_views.action_list_views import action_list_template
from .purchases_views.inventory_out_voucher_views import inventory_out_voucher_template
from .purchases_views.PO_cancellation_views import purchase_order_cancel_template
from .purchases_views.purchases_orders_views import purchase_order_template
from .purchases_views.purchases_return_views import purchase_return_template
from .purchases_views.requisition_approval_views import requisition_approval_template
from .purchases_views.requisition_orders_views import requisition_order_template
from .purchases_views.stock_vouchar_views import stock_voucher_template





urlpatterns = list(chain(
    action_list_template,
    inventory_out_voucher_template,
    purchase_order_cancel_template,
    purchase_order_template,
    purchase_return_template,
    requisition_approval_template,
    requisition_order_template,
    stock_voucher_template,
))