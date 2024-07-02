from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


# 1) Bu klasdan FORM elementlerini VALIDATE etmek ucun istifade edeceyik.  Normalda VALIDATE edilen FORM elementleri 2 hisseye ayrilir:
        #                                                                                                                               a) MODEL ile yəni, CƏDVƏL ilə əlaqəsi olmayan FORM elementleri 
        #                                                                                                                               b) MODEL ilə yəni, CƏDVƏL ilə əlaqəli olan    FORM elementleri 
# 
# 2) MODEL ilə əlaqəli olan FORM elementleri, DB-de CEDVEL-in sütunlarına tetbiq edilən VALIDATOR-lari avtomatik olaraq qəbul edir.
#    Mesel ucun GOODS qovlugunun MODELS.PY faylinin CATEGORIES() klasinda belə bir kod var:
#                                                                                           name = models.CharField(max_length=150, unique=True, verbose_name='Name')
# 
#    Burada MAX_LENGTH 150 olmalidir, NAME sahesi UNIQUE yəni mütləq yazılmalıdır deyə həmin FORM sahəsinin bu şərtlərə əməl etməsini bildirmişik. Bu FORM elementleri üçün təyin etdiyimiz VALİDATOR-dur
#    və FORM elementinə yazılan dəyərlər DB-sə göndərilmədən əvvəl VALİDATOR tərəfindən yoxlanılması üçün gərəklidir.  
# 
#  3) Yuxarıda İMPORT etdiyimiz FORMS paketidə buna görə lazımdır ki, LOGIN ve REGISTRATION ilə əlaqəli olan sahələrə girilən dəyərləri DB-sə göndərmədən əvvəl onların VALİDYLİYİNİ yoxlayaq. 
#     Həmin VALİDLIK şərtlərinin işləməsi üçün FORMS paketindən MODELFORM klasını çağıraraq USERLOGİNFORM() klasına həmin MODELFORM klasını izləsin deyə bilərik:
#                                                                                                                                                                 class UserLoginForm(forms.ModelForm):

#     Yaxud DJANGO-da LOGIN ve REGISTRATION ilə işləmək üçün, MODELFORM klasindan daha çox funksional olan AUTHENTİCATİONFORM klasindan istifadə edə bilərik.
#     Bunun üçün isə ilk öncə həmin klası İMPORT etməliyik və USERLOGİNFORM() klasına həmin klası izlə deməliyik:                                                             
#                                                                                                                  from django.contrib.auth.forms import AuthenticationForm
class UserLoginForm(AuthenticationForm):
    class Meta:
        # 4) İndi isə həmin formanın hansı MODEL ilə işləməsi gərəkdiyini yazmalıyıq. Bizim MODEL-imiz yerləşir USERS qovluğunda və adı USER-dir. Onun üçün həmin modeli İMPORT edirik və MODEL-i çağırırıq.
        model = User()

        # 5) İndi isə elə etməliyik ki, bizim CONTROLLER-imiz, bu FORMS ilə işləsin. Bunun üçün daxil oluruq    USERS/VIEWS.PY    kontrollerinə. 


