from django import forms
# 1) LOGIN ilə işimiz bitdi. İndi   REGİSTRATİON    (registration.html)   ilə əlaqəli hissəni işləmək üçün ilk öncə    'UserCreationForm'    klasını   İMPORT edirik. 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


# 2) 'UserRegistrationForm'   klası    'UserCreationForm' - klasını  bu klas özüdə    'BaseUserCreationForm'   klasını izləyir:
#                                                                                                                               BaseUserCreationForm klasında 2 sahə var:    password1 & password2
#                                                                                                                               UserCreationForm klasında isə 1 sahə var:    username
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        # 3) FİELDS sahəsində yazılan adlar ilə DB-də yazılan adlar eyni olmalıdır. 
        fields = [
                'first_name', 
                'last_name', 
                'username', 
                'email', 
                'password1', 
                'password2', 
            ]
    # 4) Şablon üçün istifadə ediləcək elementləri aşağıdakı kimi yaza bilərik ancaq keçən dərslərdə dedik ki, FRONT hissəni BACK hissədə yazmamaq yaxşıdır. Onun üçün aşağıda olan kodları kommentə alırıq və sadəcə orada qalırlar.
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

