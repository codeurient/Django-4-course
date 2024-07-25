from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'first_name', 
                'last_name', 
                'username', 
                'email', 
                'password1', 
                'password2', 
            ]

    # 1) Kommentə aldıqdan sonra isə həmin variable-lara boş   'CharField()'    metodlarını veririk. 
    first_name  = forms.CharField()
    last_name   = forms.CharField()
    username    = forms.CharField()
    email       = forms.CharField()
    password1   = forms.CharField()
    password2   = forms.CharField()



"""
    first_name = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your first name",
            }
        )
    )
        
    last_name = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your last name",
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your username",
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email address",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password"
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Repeat your password"
            }
        )
    )
"""