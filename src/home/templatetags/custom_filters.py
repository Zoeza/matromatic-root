# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def dict_get(d, key):
    return d.get(str(key), 0)
