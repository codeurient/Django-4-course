from django.db import models

# 1) DJANGO da MODEL cedvel yəni TABLE demekdir. İlk table olaraq Category-leri yaradiriq. Her Category icinde o kateqoriyaya aid PRODUCT-lar olacaq. 

# 2) CATEGORIES adinda CLASS yaradiriq ve bu class 'models.Mode' adinda daxili CLASS-i izləyəcəkdir. Bu daxili 'models.Model' CLASS içində ORM tərəfindən təmin edilən müxtəlif 
# xüsusiyyətlərə və DB ilə əlaqəni asanlaşdıran metodlara malikdir. 
class Categories(models.Model):
    # 3) Burda ise Table-da olacaq saheler (sütunlar) hansilardirsa onlarin adlarini yaziriq. Hemin sahe adlari ile birlikde onlarin tipinide yazmaq lazimdir.
    # Hemin tipler (Field types) haqqinda Django-nun saytinda etrafli qeyd edilmisdir. Meslen 'ChardFiedl' - string sahesidir ve kicik metnler ucun istifade edilir.
    # 'TextFiedl' - string sahesidir ve boyuk metnler ucun istifade edilir ve.s:  https://docs.djangoproject.com/en/5.0/ref/models/fields/
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

#* 4) Qeyd edim ki, yuxarida ID sahesini yaratmadiq. Cunki, Django-da bu sahe avtomatik olaraq yaradilir. ID sahesinin avtomatik yaranmasina sebeb olan variable, APP qovlugunda
#* SETTINGS.PY faylinin icinde yerlesir: DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 
# 5) Indi nece etmek olarki, bu CLASS-i cedvele cevirek ? Yəni, ele etmeliyik ki, ilk öncə bu CLASS göndərilsin MİGRATİON-a və həmin MİGRATİN-da olan kod ilə də DB içində cədvəl yaradılsın. 
# Bunun ucun terminalda yaziriq: python manage.py makemigration