from django.db import models
from django.contrib.auth.models import AbstractUser


# 1) USER adinda klas yaradiriq ve bu klasimiz 'AbstractUser'  adlı abstract klası izləyir. Bu AbstractUser klasinida yuxarida MANUAL İMPORT edirik. 
class User(AbstractUser):
    # 2) Bu AbstractUser klası içində bəzi sahələr mövcuddur. Onun üçün də biz digər lazım olan sahələri əlavə edəcəyik. İlk əlavə edəcəyimiz sahə İMAGE sahəsi olacaq.
    # Xatırladım ki, bütün klaslarımız yerləşir MODELS adlı paketin içində. Həmçinin İMAGE əlavə etmək üçün isifadə edəcəyimiz klass olan ImageField()  klasıda. 
    # VERBOSE_NAME ilə sütunun ADMİN paneldə
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Avatar')
    # 3) İndi isə digər MODEL-lər kimi bu MODEL-idə qeydiyyata almaliyiq ki, onu ADMİN paneldə görə bilək. Bunun üçün daxil oluruq USERS/ADMİN.PY faylına
