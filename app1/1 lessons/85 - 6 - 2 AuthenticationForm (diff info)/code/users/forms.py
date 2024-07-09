from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    # 1) 'AuthenticationForm'    klasında olan    username və password    sahələrinin DEFAULT dəyərlərini sıfırlamaq üçün həmin faylda olan kodları aşağıdakı kimi yaza bilərik:
    username = forms.CharField()
    password = forms.CharField()

    # Şəkil nömrə 2 yə bax:
    #                       <div>
    #                           <label for="id_username">Username:</label>
    #                           <input type="text" name="username" maxlength="150" required="" id="id_username">
    #                       </div>


    class Meta:
        model = User
        fields = ['username', 'password']