from django.shortcuts import render

from users.forms import UserLoginForm




def login(request):
    # 1) FORMS.PY faylında yaratdığımız   UserLoginForm()   klasını çağırırıq ki,  CONTROLLER-imiz həmin klas ilə işləyə bilsin.
    form = UserLoginForm()

    context = {
        'title' : ' Home - Authorization ',
        # 2) Sonra isə həmin FORM-u context-ə yerləşdiririk.
        'form' : form
    }
    return render( request, 'users/login.html', context )






def registration(request):
    context = {
        'title' : ' Home - Authentication '
    }
    return render( request, 'users/registration.html', context )






def profile(request):
    context = {
        'title' : ' Home - Profile '
    }
    return render( request, 'users/profile.html', context )






def logout(request):
    ...