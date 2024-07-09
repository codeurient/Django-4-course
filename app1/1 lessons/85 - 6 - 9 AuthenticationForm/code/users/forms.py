from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User


class UserLoginForm(AuthenticationForm):

    # 1) Əslində heç bu  CharField-lərdə bizə lazım deyil onlarıda kommentə ala bilərik. AuthenticationForm klası bizim üçün hər işi görür. 
    # username = forms.CharField()
    # password = forms.CharField()


    class Meta:
        model = User
        fields = ['username', 'password']