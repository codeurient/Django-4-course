from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Avatar')

# 1) Meta klasini elave ederek ADMIN panelde cedvelin adini, Admin panelde USER yazisinin tekde ve cemde nece ve hansi dilde yazilmasi gerekdiyini bildiririk.  
    class Meta:
        db_table = 'user'
        verbose_name = 'User'           # Istifadeci
        verbose_name_plural = 'Users'   # Istifadeciler

# 2) __STR__ metodu USER modelinin USERNAME sütununun dəyərini ADMİN PANEL-də əks etdirmək üçün istifadə edilir.
    def __str__(self):
        return self.username
    


# 3) NOT:      USER     cədvəlimizi yaratdıqda  elə etməliyik ki,  DJANGO   bilsin ki, biz öz    USER MODEL-imizi yaratmışıq və onu  MİGRATE etmək istəyirik.    Əks halda model-i   MİGRATE   etmək istədikdə  DNAJGO   
#              bizim model-imizi iqnor edərək, öz      AUTH_USER     model-ini MİGRATE edəcək.  
#
#              Bunun olmaması üçün ilk öncə daxil oluruq,   APP/SETTINGS.PY   faylina ve en sona duserek yazmaliyiq ki, DJANGO öz AUTH_USER modeli əvəzinə bizim model-imizi istifadə etsin:    AUTH_USER_MODEL = 'users.User'


