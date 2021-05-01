from django import forms
from url_shortener.models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def clean(self):
        data = super().clean()
        password = data.get('password')
        password_repeat = data.get('password_repeat')
        if password_repeat != password:
            self.add_error('password_repeat', forms.ValidationError('رمزعبورها یکسان نیستند!', code='password_match'))
        return data

class UserProfile(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('birthdate', 'photo')

