from django.shortcuts import render
from url_shortener.models import URL, Code
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    return render(request, 'url_shortener/home.html')


def short_url(request, code):
    url = get_object_or_404(Code, slug=code).target
    url.increase_visits()
    return HttpResponseRedirect(url.address)

def register(request):
    pass
