from django.shortcuts import render
from url_shortener.models import URL, Code
from url_shortener.forms import UserForm, UserProfileForm
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
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save()
            profile.user = user
            if 'picture' in request.FILES:
                profile.photo = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context_dict = {'user_form': user_form, 'profile_form': profile_form,
                    'registered': registered}
    return render(request, 'url_shortener/register.html', context_dict)
