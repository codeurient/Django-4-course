from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, You are now logged in")
                # 1) Deməli sayta giriş etmədən URL yerində   'user/profile'   yazdıqda LOGİN.HTML şablonuna yönlənirik və url yerində belə bir link görürük: http://127.0.0.1:8000/user/login/?next=/user/profile/
                # 2) Sonra saytda giriş etmək üçün NAME və PAROL-u daxil edərək ENTER düyməsini basırıq. Bu vaxt ŞABLON-dan, POST metodu vasitəsi ilə URL yerindəki linkin   NEXT    parametrinin   '/user/profile/'   dəyərini 
                #    digər dəyərlər ilə birlikdə ötürmüş oluruq hal-hazırda içində olduğumuz    USERS/VIEWS.PY    controller-inin LOGIN() metoduna. 
                # 
                # 3) Sonra şərt qoşuruq ki, əgər şablondan POST metodu ilə GET() edilən 'NEXT' parametri varsa, RETURN olsun HttpResponseRedirect() metodu.   HttpResponseRedirect() metoduda bizi yönləndirir  'user/profile'  linkinə.
                #   
                #   GET() metodunun 1ci parametri NEXT parametridir. 2ci parametri isə əgər belə bir parametr yoxdursa default olaraq NONE olsun yəni heçnə baş verməsin.
                # 
                #   request.POST.get('next') kodunun bizə verdiyi nəticə 'user/profile' - dir.
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                # 4) Sayta normal LOGİN olaraq daxil olmaq istədikdə onda aşağıdakı   HttpResponseRedirect()  metodu işləyir. LOGİN olmadan URL yerində    'user/profile'    etmək istədikdən  sonra daxil ola bilməyərək LOGİN.HTML 
                #    səhifəsinə yönlənib sonra sayta daxil olmaq istədikdə onda yuxarıdakı  HttpResponseRedirect() metodu işləyir.
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
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, You are now registered and logged in")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {
        'title' : ' Home - Authentication ',
        'form' : form,
    }
    return render( request, 'users/registration.html', context )


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            messages.success(request, "Profile successfully updated")
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title' : ' Home - Profile ',
        'form' : form,
    }
    return render( request, 'users/profile.html', context )
@login_required


def logout(request):
    messages.success(request, f"{request.user.username}, You are now logged out")
    auth.logout(request)
    return redirect(reverse('main:index'))