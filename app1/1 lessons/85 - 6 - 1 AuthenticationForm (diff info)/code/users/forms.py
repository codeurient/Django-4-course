from django import forms

from django.contrib.auth.forms import AuthenticationForm

from users.models import User

# 1) Indi isə yeni qayıdaq   'AuthenticationForm'    mövzusuna.    İlk öncə klavyaturanın CTRL düyməsini basılı tutaraq aşağıdakı    'AuthenticationForm'    sözünün üzərində mausun sağ düyməsini klikləyirik.  FORMS.PY  adında daxili
#    Django faylı açılacaq. Bu faylda həmin    'AuthenticationForm'   klası yaradılmışdır və içində 2 dənə VARİABLE var.   username və password.     
#    Bunlar bizim INPUT tag-lərimizin sahələridir və həmin USERNAME, PASSWORD və.s adları USER() modelimizdəki adlar ilə eyni olmalıdır. Çünki USER() modeli əslində bizim DB-də olan CƏDVƏLİMİZ-dir və həmin cədvəlin sütunlarının (sahələrin)
#    adları bu cür təyin edilmişdir. Yəni, username, password və.s kimi. 
# 
#    Deməli    'AuthenticationForm'    klasında   sadəcə 2 sahə qeyd edilmişdir. Və bu sahələrini yəni bu İNPUT tag-lərinə kod vasitəsi ilə atributlar, dəyərlər təyin edilmişdir. Məsələn bir İNPUT tag-inin nələri ola bilər ? Default
#    olaraq    'AuthenticationForm'    klasında bunlar qeyd edilib. Görmək üçün isə proqramı işə salaq və brauzerdə İNSPECT pəncərəsini açaraq baxaq. Nə qeyd edildiyini burda yazıda da göstərəcəm, şəkil nömrə 2ni açaraq baxmaqda olar:
#                                                                                                           Type, name, autocapitalize, maxlength və.s
#                                                       <div>
#                                                           <label for="id_username">Username:</label>
#                                                           <input type="text" name="username" autofocus="" autocapitalize="none" autocomplete="username" maxlength="150" required="" id="id_username">
#                                                       </div>

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']