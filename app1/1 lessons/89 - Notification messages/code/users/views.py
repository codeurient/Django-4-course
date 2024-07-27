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
                # 2) LOGIN olduqdan sonra istifadeciye mesaj gostermek ucun MESSAGES modulundan istifade ede bilerik:                                           from django.contrib import auth, messages
                messages.success(request, f"{username}, You are now logged in")
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
            # 3) Eyni mesaji qeydiyyatdan kecdikden sonra da gostermek ucun burada da yaziriq.
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
            # 4) Ve UPDATE etdikden sonra da mesaj gostermek ucun yaziriq
            messages.success(request, "Profile successfully updated")
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        # 1) Saytan LOG OUT olduqdan sonra URL yerinde bele yazdiqda AttributeError xeta mesaji ile qarsilasiriq: http://127.0.0.1:8000/user/profile/
        # Bunun PROFILEFORM() klasinda yazdigimiz INSTANCE parametridir. Cunki bu parametr USER modelinden melumatlari input sahelerinde eks etdirmek ucun istifade edilir.
        # Ancaq biz PROFILE sehifesini ve hemin melumatlari ancaq LOGIN olduqda gore bilmeliyik. 
        # 
        # LOGOUT olduqdan sonra qeydiyyatdan kecmiyen yaxud sayta daxil olmuyan istifadecilerə bezi controller-lere daxil olmani qisitlamaq lazimdir. 
        # 
        # Bunu etmek ucun LOGİN_REQUİRED adli Dekaratordan istifade ede bilerik. Hemin dekaratoru yuxarida IMPORT etmek lazimdir:                   from django.contrib.auth.decorators import login_required
        # Artiq xeta mesaji evezine PAGE NOT FOUND goreceyik. Bu normaldir. 
        form = ProfileForm(instance=request.user)
    context = {
        'title' : ' Home - Profile ',
        'form' : form,
    }
    return render( request, 'users/profile.html', context )
@login_required


def logout(request):
    # 5) Cixis etdikde de mesaj gostermek ucun yaziriq.   Bunlari yazdiqdan sonra daxil oluruq TEMPLATES - INCLUDES - NOTIFICATIONS.HTML faylina. Ve bu fayla lazimli HTML tag-lerimizi yaziriq ki, CIXIS ve.s etdikde gosterilecek alert mesajları hemin tag-lere yazdirilsin ve bize gösterilsin.
    messages.success(request, f"{request.user.username}, You are now logged out")
    auth.logout(request)
    return redirect(reverse('main:index'))