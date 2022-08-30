from django.urls import path
from itertools import chain
from .sales_views.properties_views import properties_templates
from .sales_views.upgrade_property_price_views import upgrade_property_prices_templates
from .sales_views.property_sale_views import property_sale_templates
from .sales_views.master_delete_property_views import master_delete_property_templates
from .sales_views.additional_charges_views import additional_charges_templates
from .sales_views.agent_commission_views import agent_commission_templates
from .sales_views.buy_back_views import buy_back_templates
from .sales_views.installment_plan_views import installment_plan_A_templates
from .sales_views.installment_plan_B_veiws import installment_plan_B_templates
from .sales_views.surcharge_waiver_views import surcharge_waiver_templates
from .sales_views.merger_views import property_merger_templates
from .sales_views.cancellation_veiws import property_cancellation_templates
from .sales_views.transfer_views import property_transfer_templates
from .sales_views.property_surcharge_views import property_surcharge_templates





app_name = 'Sales'

urlpatterns = list(chain(properties_templates, upgrade_property_prices_templates,property_surcharge_templates,
                        property_sale_templates, master_delete_property_templates,
                        additional_charges_templates, agent_commission_templates, buy_back_templates,
                        installment_plan_A_templates, installment_plan_B_templates, surcharge_waiver_templates,
                        property_merger_templates, property_cancellation_templates, property_transfer_templates, master_delete_property_templates))