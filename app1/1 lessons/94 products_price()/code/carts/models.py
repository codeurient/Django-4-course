from django.db import models
from goods.models import Products
from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="User") 
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Product")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Quantity")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Created date")

    class Meta:
        db_table = "cart" 
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    # 1) Indi isə, məhsulun miqdarını vurmaq lazımdır məhsulun qiymətinə. Məhsulun 2 qiyməti vardır:
    #                                                                                                 a) endirimsiz qiyməti
    #                                                                                                 b) endirimli qiyməti
    # 
    #    Məhsulun qiyməti ilə bağlı metodu əvvəlcədən yazmışıq      GOOODS / MODELS.PY      faylının içinə və hal-hazırda içində olduğumuz fayla PRODUCTS qovluğunu İMPORT etdiyimizdən
    #    həmin məhsulun qiymətini hesablamaq üçün gərəkli olan     SELL_PRİCE()    metodunu çağıraraq istifadə edə bilərik. 
    #   
    #    İndi bir metod yaradırıq və bu metod RETURN edəsidir məhsulun miqdarının qiymətinə olan hasilini. Bu metod eyni olan bir yaxud bir neçə məhsulun miqdarını hesablamaq üçündür.
    #    Bizə əlavə olaraq bir metod daha lazımdır ki, səbətdə olan birdən çox fərqli məhsulların ümumi qiymətini və miqdarını hesablasın. 
    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
   
    def __str__(self):
        return f'Cart {self.user.username} | Product {self.product.name} | Quantity {self.quantity}'
    
