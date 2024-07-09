from django import forms

# 1) USERS - TEMPLATES - USERS - LOGİN.HTML   faylında, özümüzün yazdığı İNPUT tag-lərini kommentə alaraq, DJANGO-nun 'AuthenticationForm' klası ilə vermiş olduqlarını istifadə etdik. Həmin DJANGO-nun vermiş olduqları 
#    iki dənə sahədən ibarət idi. 'username' və 'password'.   Həmin sahələri 'AuthenticationForm' üçün artırmaq olar və bunun birdən çox yolu var ancaq çox qarışıqdır. 
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


# 2) İndi isə gəlin bu 'AuthenticationForm'  klasını pozaq və   'FORMS'   modulundakı   'MODELFORM'    klasını izləyək.    
#    
#    Bu 2 class arasındakı fərq nədir bəs ?   AuthenticationForm:
#                                                                   a) DJANGO-nun istifadəçi kimliyini yoxlamaq üçün yaradılmış xüsusi daxili klasdır.                                                                                      
#                                                                   b) 2 sahədən ibarətdir: username & password                                                                                  
#                                                                   c) Sadəcə bu sahələrin mövcudluğunu avtomatik yoxlayaraq sistemə giriş etmək üçün istifadə edilir.                                                                            
#                                                                   d) Əlavə konfiqurasiyalara ehtiyac qalmır.
#                                               
#                                             ModelForm:
#                                                                   a) DJANGO-nun hər hansısa bir MODEL-inə əsaslanan formlar yaratmaq üçün istifadə edilən klasdır.
#                                                                   b) Müəyyən bir modelin sahələrinə qarşılıq gələn form sahələrini avtomatik yaratmaq üçün istifadə edilir. Bizim modelimiz USER()-dir.
#                                                                   c) Mütləq müəyyən bir model ilə əlaqələndirilməlidir.
#                                                                   c) Hansı modelin istifadə ediləcəyi META klasından bildirilir və əlavə sahələr yaratmaq yaxud mövcud sahələri inkişaf etdirmək mümkündür. 
# 
# 
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        # 3) 'MODELFORM'  klasından istifadə edərək form üçün istifadə ediləcək sahələri yaradırıq. Bu sahələr USER() modelində qeyd edilən sahələrin adları olmalıdır. USER() modeli bizim TABLE-ımızdır və bu cədvəldə 
        #     a) username
        #     b) password
        #     c) image
        #     d) is_staff və.s çoxlu sahələr var. Həmin Cədvəldəki sahələrin adlarını isə aşağıdakı kimi   FIELDS   adında LİST yaradaraq bu list-in içinə yazmaq lazımdır ki, şablonda həmin sahələr əks olunsun.
        fields = ['username', 'password']