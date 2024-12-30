from django import template
register = template.Library()

@register.filter
def type_filter(obj):
    return type(obj).__name__