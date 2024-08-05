from django.db import models
from goods.models import Products
from users.models import User

# 1) İstifadə tərəfindən sifariş edilən məhsulları, DB-də necə saxlayacağıq ? Bunun ucun necə bir MODEL yaratmaq lazımdır ?


# 2) Bunun üçün bir neçə qayda vardır. Və bizim etməyəcəyimiz qayda odur ki, bütün məlumatları DB-də bir sütunda JSON kimi saxlayaq. 
#    JSON kimi saxlamaq əslində, iş prinsipini başa düşmək üçün rahat qaydadır ancaq onunla iş görmək çətindir. 


# 3) Yaxşı qayda odur ki, istifadəçinin sifariş etdiyi hər məhsul üçün DB-də ayrı-ayrı qeyd-lər yaradaq. 
class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="User") # Birdaha qisaca qeyd edim ki, verbose_name parametri Admin panelde sahelere öz istediyimiz dildə ad vermək üçün istifadə edilir.
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Product")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Quantity")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Created date")

    class Meta:
        db_table = "cart" # Cedvelin DB-de nece adlanacagini teyin edirik.
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

   
    def __str__(self):
         # 4) __STR__()   metodu ilədə Admin paneldə başa düşülən açıxlama stringini yazdırırıq. 
        return f'Cart {self.user.username} | Product {self.product.name} | Quantity {self.quantity}'
    

# 5) Sifarişləri DB-də saxlamaq olduğu kimi, FRONT tətərəfində də, yəni İstifadəçinin komputerinin COOKİE-lərində də saxlamaq olar. Ancaq bunun minusu ondadır ki, sifariş cookie-lərdə olduqda həmin sifarişlərin
#    analitikasını aparmaq olmur. Yaxud məhəsələn istifadəçi səbətə məhsul əlavə etdi ancaq məhsulu sifariş etmədən səbətdə günlərlə saxlayır və biz istifadəçiyə endirim etmək istəyirik ki, məhsul sifariş edilsin. 
#    Ancaq məhsulun sifarişi Cookie-lərdə olduqda bunu etmək olmur. 

# 6) Sonra yuxarıda    CREATED_TİMESTAMP    sütununu onun üçün əlavə etdik ki, məhsulun səbətə əlavə edildiyi gündən 3-4 gün keçsə ona xəbərdarlıq mesajı göndərə bilək. 
#    Yaxud 1 ay boyunca sifariş edilməyən məhsulu DB-dən silə bilək.

