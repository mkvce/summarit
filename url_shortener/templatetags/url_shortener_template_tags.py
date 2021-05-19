from django import template
from url_shortener.forms import URLForm

register = template.Library()


@register.inclusion_tag('url_shortener/navbar.html')
def navbar(user):
    return {'user': user}


@register.inclusion_tag('url_shortener/url_form.html')
def url_form(form=URLForm()):
    return {'form': form}
