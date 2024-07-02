from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import render
from django.urls import reverse
from users.forms import UserLoginForm


def login(request):
    # 1) Bu aşağıda yazdığımız kod Dokumentasiyadan əldə etdiyimiz standart koddur. Deməli, biz səhifədə BUTTON tag-indən fərqli olan digər istənilən keçidə kliklədikdə, MƏSƏLƏN: header hissədə olan 'Log in' sözündə, onda GET sorğu
    #    göndərmiş hesab ediləcəyik və İF konstruktoru FALSE verəcək onun üçün ELSE işləyərək ekranda USERNAME və PASSWORD sahələrini görəcəyik. 
    # 
    # 2) Sonra İNPUT sahələrinə dəyər daxil edərək BUTTON-u klikləsək POST sorğu göndəriləcək və İF konstruktorun içinə daxil olacağıq.
    if request.method == 'POST':
        # 3) İNPUT sahələrinə daxil edilən dəyərləri DATA atributuna verərək UserLoginForm() klası ilə göndəririk qarşı tərəfə. 
        form = UserLoginForm(data=request.POST)
        # 4) Sonra IS_VALID() metodu ilə sahəyə daxil edilən dəyərlərin VALİD-liyini yoxlayırıq. Əgər hər şey doğru daxil edilibdirsə TRUE qayıdacaq və biz irəli gedəcəyik. Məsələn EMAİL-i daxil etdikdə @ simvolu yazılıbdırmı və.s kimi.
        if form.is_valid():
            # 5) Daxil edilən adı USERNAME variable-ına yerləşdiririk.
            username = request.POST['username']
             # 6) Daxil edilən şifrəni PASSWORD variable-ına yerləşdiririk.
            password = request.POST['password']
             # 7) AUTH modulunu İMPORT edərək AUTHENTİCATE() metodu ilə yoxlayırıq ki, DB-in USERNAME və PASSWORD sahələrində həmin adda və şifrədə istifadəçi varmı ?! Əgər varsa, USER variable-ı həmin istifadəçi obyektini əldə edəcək.
             #    Yəni istifadəçini digər bütün məlumatları ilə əldə edərək USER variable-ına yerləşdiririk.    
            user = auth.authenticate(username=username, password=password)
            # 8) Belə bir istifadəçinin olması TRUE mənasına gəlir və İF konstruktoru işləyir.
            if user:
                # 9) Və bu cür istifadə mövcud olduğu üçün AUTH modulunun LOGİN() funksiyası ilə həmin istifadəçinin sayta daxil olmasına icazə veririk. 
                auth.login(request, user)
                # 10) Daxil olduqdan sonra isə HttpResponseRedirectBase() klası ilə istifadəçini Ana səhifəyə yönləndiririk. Burada REVERSE() metodundan onun üçün istifadə etmişik ki, HttpResponseRedirectBase() klasında, uzun URL marşrut
                #     yazmayaq. Yəni, şablonlarda olduğu kimi qısa yaza bilək və həmin qısa yazılışı REVERSE() metodu lazımlı URL adresə avtomatik çevirsin. 
                return HttpResponseRedirectBase(reverse('main:index'))
    else:
        form = UserLoginForm()


    context = {
        'title' : ' Home - Authorization ',
        # 11) IS_VALID() olduqda İF içində nə baş versin dedik. Bəs əgər İstifadəçi, input sahəsində VALİD olmuyan dəyərlər yazarsa onda nə baş verəcək? Yuxarıda    'if form.is_valid()'   üzərində daxil etdiyimiz dəyərlər mövcuddur.
        #     Həmçinin xətalı girilən dəyərlər. Bu dəyərlər ötürülür bu hal-hazırda olduğumuz yerin bir sətr altındakı  'form' : form   adlı xassəyə ordan da şablona və xətalı girilən dəyər haqqında məlumatıda şablonda əks etdirə
        #     bilirik. Xəta mesajlarının göstərilməsini hələki düzəltməmişik ancaq birazdan edəcəyik. Hələki proqramı işə salaq və nə əldə edəcəyimizə baxaq. 
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