from itertools import chain

from .sms_views import sms_templates

app_name = 'SMS'

urlpatterns = list(chain(
            # SMS Templates URLS
                    sms_templates
                        ))  