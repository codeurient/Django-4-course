from django.contrib import auth
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
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title' : ' Home - Authentication ',
        'form' : form,
    }
    return render( request, 'users/registration.html', context )




# 1) SUBMIT edilen deyerleri PROFILE() metodunun REQUEST parametrine gelir.
def profile(request):
    if request.method == 'POST':
        # 2) PROFILEFORM() klasinda 3 parametr qeyd edirik: 
        #                                                   a) DATA parametri FORM məlumatlarını ehtiva edir və bu məlumatları validate etmək üçün istifadə edilir. 
        #                                                   b) İNSTANCE parametri hansi MODEL-i update edəcəyimizi bildirmək üçün istifadə edilir. Mövcud istifadəçini update etmək istədikdə bu parametrəyə verilən dəyər REQUEST.USER-dir.
        #                                                   c) FİLES parametri isə POST metodu ilə göndərilən sənədləri ehtiva edir. request.FILES içində FORM ilə göndərilən bütün sənədlər mövcuddur. Həmçinin şəkillərdə. 
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        # 3) Əks halda yəni SUBMİT edilmədikdə əgər input sahələrində əvvəlcədən DB-də mövcud olan məlumatları əks etdirmək istəyiriksə onda ProfileForm() klasına İNSTANCE parametrini verməliyik. 
        form = ProfileForm(instance=request.user)

    context = {
        'title' : ' Home - Profile ',
        # 4) Son olaraq məlumatları şablona əks etdirmək üçün FORM adı ilə həmin data-ları göndəririk. 
        'form' : form,
    }
    return render( request, 'users/profile.html', context )







def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))