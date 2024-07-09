from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    # 1) Yaxud    'AuthenticationForm'    klasında olan    username və password    sahələrini modifikasiya edə bilərik.   Bunun üçün ilk öncə    'AuthenticationForm'    klasından həmin variable-ları kopyalayaraq bura yerləşdiririk.
    #    Sadəcə UsernameField() klasının adını CharField() ilə əvəz edirik. Digər hər şey olduğu kimi qala bilər.


    # 2) Modifikasiya etmək dedikdə nəzərdə tutulan şey mövcud parametrləri silmək yaxud daha çox fərqli parametrlər əlavə etmək nəzərdə tutulur. Məsələn aşağıda LABEL və STRİP parametrlərini silirik. Sonra isə, 
    #    USERS - TEMPLATES - USERS - LOGIN.HTML faylında kommentə aldığımız FORM elementlərinə bənzər atributlar və dəyərlər əlavə edərək modifikasiya edirik aşağıdakı sahələri. Yəni, aşağıdakıları oxşadırıq LOGIN.HTML faylında olan
    #    kommentə aldığımız özümüzün FORM elementlərinə:
    #                                                     'class' : 'form-control'                  - yazaraq class       atributu ve ona deyer elave edirik
    #                                                     'placeholder' : 'Enter your username'     - yazaraq placeholder atributu ve ona deyer elave edirik
    #                                                     required                                  - yazmağa ehtiyac yoxdur çünki sahənin mütləq dolu olmasının vacibliyi DB-dən götürüləcək. Çünki forms faylı model ilə bağlantılıdır. və.s
    #                                                     
    #                                                     
    #                                                     
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True,
                                                             'class' : 'form-control',
                                                             'placeholder' : 'Enter your username',})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                                             'class' : 'form-control',
                                                             'placeholder' : 'Enter your password',}) 
    )

    # 3) Proqramı işə salaraq baxdıqda input tag-lərimizi səliqəli bir şəkildə görəcəyik ancaq yenədə bəzi xoşa gəlmiyən əksiklər var. Məsələn, tag-lər bir-birinə yapışıqdır. Şəkil nömrə 2də olduğu kimi. Və bunu düzəltmək üçün
    #    LOGİN.HTML şablonunda olan     {{ form }}      xassənin önünə    'AS_P'    adında     daxili DJANGO  qaydasını əlavə etmək olar     {{ form.as_p }}.       Ancaq biz belə etməyəcəyik. 
    # 
    # 
    # 


   


    class Meta:
        model = User
        fields = ['username', 'password']