from django.shortcuts import render




def login(request):
    context = {
        'title' : ' Home - Authorization '
    }
    # 1
    return render( request, 'users/login.html', context )






def registration(request):
    context = {
        'title' : ' Home - Authentication '
    }
    # 2
    return render( request, 'users/registration.html', context )






def profile(request):
    context = {
        'title' : ' Home - Profile '
    }
    # 3
    return render( request, 'users/profile.html', context )






def logout(request):
    ...