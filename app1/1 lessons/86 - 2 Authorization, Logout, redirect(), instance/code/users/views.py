from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()


    context = {
        'title' : ' Home - Authorization ',
        'form' : form
    }
    return render( request, 'users/login.html', context )



def registration(request):
    if request.method == 'POST':
        # 1) UserRegistrationForm() metodu ilə hansı data-ları qeydiyyata alacağımızı bildiririk.
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # 2) Əgər FORM elementleri VALİD-dirsə onda həmin məlumatları DB-sə SAVE() edirik.
            form.save()
            # 3) Qeydiyyatdan keçdikdən sonra LOGİN ve PASSWORD daxil etmədən bir başa sayt daxil olmaq üçün yazırıq:   user = form.instance  
            #                                                                                                                                FORM variable-ında bütün sahələr var
            #                                                                                                                                İNSTANCE  ilə qeydiyyatdan keçən istifadəçini əldə edirik.
            # 
            # Yəni, SAVE() metodu, FORM məlumatlarını MODEL obyektinə yaddaşa yazır və bu MODEL obyektini həmin məlumatlar ilə birlikdə əldə etmək üçün İNSTANCE variable-ından istifadə edirik. 
            user = form.instance
            # 4) Sonra isə    LOGİN()    metodu ilə bu USER-in giriş etməsini deyirik sonra da HttpResponseRedirect() metodu ile istifadecini basqa sehifeye yonlendiririk. 
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    # 5) Əgər istifadəçi sayta təzəcə daxil oldusa,    UserRegistrationForm()    metodu ona boş form elementlərini göstərəck.
    else:
        form = UserRegistrationForm()

    context = {
        'title' : ' Home - Authentication ',
        # 4) 
        'form' : form,
    }
    return render( request, 'users/registration.html', context )



def profile(request):

    context = {
        'title' : ' Home - Profile '
    }
    return render( request, 'users/profile.html', context )

def logout(request):
    # 6) Hesabdan çıxış etmək üçün isə LOGOUT() metodundan istifadə edirik.
    auth.logout(request)
    # 7) Çıxış etdikdən sonra başqa səhifəyə yönlənmək üçün isə HttpResponseRedirect() yaxud ona alternativ olan REDİRECT() metodundan istifadə edirik.
    return redirect(reverse('main:index'))