from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Електронна пошта')
    first_name = forms.CharField(max_length=30, required=True, label='Ім\'я')
    last_name = forms.CharField(max_length=30, required=True, label='Прізвище')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'username': 'Ім\'я користувача',
            'password1': 'Пароль',
            'password2': 'Підтвердження паролю',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class WeatherSearchForm(forms.Form):
    city = forms.CharField(
        max_length=100,
        required=True,
        label='Місто',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть назву міста (наприклад: Київ, Львів, Харків)'
        })
    ) 