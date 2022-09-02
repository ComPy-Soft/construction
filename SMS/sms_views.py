from django.shortcuts import render
from django.urls import path

#################################### Generate SMS ############################################

def generate_sms(request):
    return render(request, 'SMS/generate_sms.html')


#################################### Manage SMS ###############################################

def manage_sms(request):
    return render(request, 'SMS/manage_sms.html')

#################################### SMS Settings ##############################################

def sms_settings(request):
    return render(request, 'SMS/sms_settings.html')

#################################### SMS Templates #############################################

sms_templates = [
    path('generate_sms/', generate_sms, name='generate_sms'),
    path('manage_sms/', manage_sms, name='manage_sms'),
    path('sms_settings/', sms_settings, name='sms_settings'),
]