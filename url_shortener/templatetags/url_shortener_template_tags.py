from django import template

register = template.Library()


@register.inclusion_tag('url_shortener/navbar.html')
def navbar(user):
    return {'user': user}
