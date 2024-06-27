from django.shortcuts import render


# 1) Asagida metodlarimizi yaratdiq. Bu metodu cagirdiqda onun REQUEST parametri deyerler qebul edecek.
#    context adlı DİCT-in içində şablona göndəriləcək xassə və dəyərlərimizi yerləşdiririk
#    RENDER() metodu ilə də REQUEST parametrini ve CONTEXT dict-ini render edirik şablona. Ancaq qeyd etməmişik hələki hansı şablona. Bunu RENDER() metodunun 2ci parametrində qeyd edəcəyik.



def login(request):
    context = {
        'title' : ' Home - Authorization '
    }
    return render( request, '', context )






def registration(request):
    context = {
        'title' : ' Home - Authentication '
    }
    return render( request, '', context )






def profile(request):
    context = {
        'title' : ' Home - Profile '
    }
    return render( request, '', context )






def logout(request):
    ...


