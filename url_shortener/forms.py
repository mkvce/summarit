from django import forms
from url_shortener.models import UserProfile
from django.contrib.auth.models import User


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
            raise forms.ValidationError('رمزعبورها یکسان نیستند!',
                                        code='password_match')
        return data


class UserProfileForm(forms.ModelForm):
    birthdate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'}), label='تاریخ تولد')

    class Meta:
        model = UserProfile
        fields = ('birthdate', 'photo')
