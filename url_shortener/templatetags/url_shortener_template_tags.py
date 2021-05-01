from django import template
from django.urls import reverse

register = template.Library()

@register.inclusion_tag('url_shortener/navbar.html')
def navbar(user):
    if not user.is_authenticated:
        nav_items = {
            'ورود': '#',
            'ثبت نام': '#',
            'درباره ما': '#',
        }
    else:
        nav_items = {
            'آپشن ۱': '#',
            'آپشن ۲': '#',
            'آپشن ۳': '#',
        }
    return {'nav_items': nav_items}
