from django import forms
from django.core.exceptions import ValidationError
from url_shortener.models import UserProfile, URL
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(), label="نام")
    last_name = forms.CharField(widget=forms.TextInput(), label="نام خانوادگی")
    username = forms.CharField(widget=forms.TextInput(), label="نام کاربری")
    email = forms.EmailField(widget=forms.EmailInput(), label="ایمیل")
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6, label='گذرواژه')
    password_repeat = forms.CharField(widget=forms.PasswordInput(), min_length=6,
                                      label='تکرار گذرواژه')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def clean_password_repeat(self):
        data = self.cleaned_data
        if data.get('password_repeat') != data.get('password'):
            raise ValidationError(_('گذرواژه‌ها یکسان نیستند!'),
                                  code='password_match')
        return data


class UserProfileForm(forms.ModelForm):
    birthdate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}),
                                    label='تاریخ تولد')

    class Meta:
        model = UserProfile
        fields = ('birthdate', 'photo')


class URLForm(forms.ModelForm):
    address = forms.URLField(max_length=256,
                             widget=forms.TextInput(attrs={'placeholder': 'آدرس لینک', 'class': 'form-control'}))
    label = forms.CharField(max_length=128,
                            widget=forms.TextInput(attrs={'placeholder': 'برچسب', 'class': 'form-control'}))

    class Meta:
        model = URL
        fields = ('address', 'label')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label="نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6, label="گذرواژه")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
