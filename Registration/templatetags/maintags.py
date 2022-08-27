from atexit import register
from django import template
from django.utils.html import escape, mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def get_PagesNames(context):
    context['PageNameList'] = ['add_customers','manage_customers']
    return mark_safe(context['PageNameList'])