from django.shortcuts import render, get_object_or_404, redirect
from url_shortener.models import URL, Code
from url_shortener.forms import UserForm, UserProfileForm, UserLoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


# Create your views here.


def home(request):
    return render(request, 'url_shortener/home.html')


def short_url(request, code):
    url = get_object_or_404(Code, slug=code).target
    url.increase_visits()
    return redirect(url.address)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'photo' in request.FILES:
                profile.photo = request.FILES['photo']
            profile.save()
            login(request, user)
            return redirect('url_shortener:home')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    context_dict = {'user_form': user_form, 'profile_form': profile_form,
                    'registered': registered}
    return render(request, 'url_shortener/register.html', context_dict)


def user_login(request):
    login_form = UserLoginForm()
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('url_shortener:home')
                else:
                    login_form.add_error(None, ValidationError("حساب کاربری شما غیر فعال است", code='inactive'))
            else:
                print("Invalid login details: {0}, {1}".format(username, password))
                login_form.add_error(None, ValidationError("نام کاربری یا رمز عبور صحیح نیست", code='invalid'))
    elif request.user.is_authenticated:
        return HttpResponse("شما قبلا وارد شده‌اید!")
    context_dict = {'login_form': login_form, }
    return render(request, 'url_shortener/login.html', context_dict)


@login_required()
def user_logout(request):
    logout(request)
    return redirect('url_shortener:login')
