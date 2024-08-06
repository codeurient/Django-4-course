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
        
                redirect_page = request.POST.get('next', None)
                # 1) if redirect_page:                                      redirect_page-in None olmadığını yoxlayır. Əgər NEXT parametri varsa TRUE qayıdacaq.
                # 2) if redirect_page != reverse('users:logout'):           redirect_page-in logout səhifəsinin URL-si olmadığını yoxlayır və deyilsə TRUE verir.
                if redirect_page and redirect_page != reverse('users:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
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



def users_cart(request):
    return render(request, 'users/users_cart.html')


def logout(request):
    messages.success(request, f"{request.user.username}, You are now logged out")
    auth.logout(request)
    return redirect(reverse('main:index'))




