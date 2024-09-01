from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
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

    first_name  = forms.CharField()
    last_name   = forms.CharField()
    username    = forms.CharField()
    email       = forms.CharField()
    password1   = forms.CharField()
    password2   = forms.CharField()



class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        )
        image       = forms.ImageField(required=False)
        first_name  = forms.CharField()
        last_name   = forms.CharField()
        username    = forms.CharField()
        email       = forms.CharField()

"""
        # 1) Bu aşağıdakı variantı onun üçün yazdıq ki, əgər birdən şablon üçün lazım olan class atributlarını yaxud dəyərlərləri backend istifadə edərək yazmaq istəyən olar. 
        #    Bunları kommentə alırıq indi və digər özümüz istifadə edən variantı yuxarıda yazırıq.
        # image = forms.ImageField(
        #     widget=forms.FileInput(attrs={"class" : "form-control"}), required=False
        # )

        # first_name = forms.CharField(
        #     widget=forms.TextInput(
        #         attrs={
        #             "class" : "form-control",
        #             "placeholder" : "Enter your name",
        #         }
        #     )
        # )

        # last_name = forms.CharField(
        #     widget=forms.TextInput(
        #         attrs={
        #             "class" : "form-control",
        #             "placeholder" : "Enter your surname",
        #         }
        #     )
        # )

        # username = forms.CharField(
        #     widget=forms.TextInput(
        #         attrs={
        #             "class" : "form-control",
        #             "placeholder" : "Enter your username",
        #         }
        #     )
        # )

        # email = forms.CharField(
        #     widget=forms.EmailInput(
        #         attrs={
        #             "class" : "form-control",
        #             "placeholder" : "Enter your email",
        #         }
        #     )
        # )
"""