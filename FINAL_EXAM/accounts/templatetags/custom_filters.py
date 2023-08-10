from django import template

register = template.Library()


@register.filter
def placeholder(value, token):
    value.field.widget.attrs['placeholder'] = token
    return value


@register.filter
def is_staff_or(condition_value, user):
    return condition_value or user.is_staff