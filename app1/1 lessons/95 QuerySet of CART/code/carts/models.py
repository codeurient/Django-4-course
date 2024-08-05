from django.db import models
from goods.models import Products
from users.models import User

# 2) Bizdə indi QUERYSET vasitəsi ilə bu məhsulları əldə edəcəyik. Bunun üçün aşağıdakı CART() klasına xidmət edəcək öz klasımızı yaradırıq.
class CartQueryset(models.QuerySet):
    # 4) İlk metodumuz səbətdə olan bütün məhsuların ümumi qiymətini hesablamaq üçün olacaq
    def total_price(self):
        # 5) TOTAL_PRICE() metodunun SELF parametri bizə cari obyekt olan CartQueryset()-i verir. Bu obyekt isə bizə  QuerySet  obyektini verir.  QuerySet  obyekti isə CART modelimizidir. Çünki aşağıda CART() obyektinin içində belə bir kod
        #    yazmışıq:  objects = CartQueryset.as_manager()    ....... Django-da QuerySet clası yaradıb onu modelin manager-i kimi təyin etdikdə, Django avtomatik olaraq, QuerySet class-ının hansı model üçün işləyəcəyini avtomatik bilir.
        # 6) Beləliklə SELF parametrində səbətdə olan məhsulların obyektləri var. FOR döngüsü ilə bu obyektləri əldə edirik və bizə lazım olan PRODUCTS_PRİCE() metodu vasitəsi ilə bütün məhsulların qiymətini cəmləyirik. 
        return sum(cart.products_price() for cart in self)
    
    # 7) Bu metod isə səbətə əlavə edilən ümumi məhsulların miqdarını vizə verəcək
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


# 1) Hal-hazırda aşağıda yazdığımız kod 1 istifadəçi üçün bir yaxud birdən çox məhsul əlavə edir həmin istifadəçinin səbətinə. Məhsul sayı 1 yaxud 1-dən çox olsa belə həmin məhsullar avtomatik olaraq
#    Django-nun QUERYSET adlı sistemində yaddaşa həkk edilir. QUERYSET nədir ?  Djangonun QUERYSET sistemi Python ilə DB arasında əlaqəni qurmağa kömək edən ORM sistemidir. DB sorğularının nəticəsi həmin 
#    bu QUERYSET sistemi tərəfindən qəbul edilir. Bizdə QUERYSET-in içindən bu nəticələri əldə edə bilirik. 

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="User") 
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Product")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Quantity")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Created date")

    class Meta:
        db_table = "cart" 
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    # 3) Sonra CART() klasının içində OBJECTS adlı variable yaradaraq CARTQUERYSET() klasımız vasitəsi ilə AS_MANAGER() metodunu çağırırıq ki, QUERYSET klasının sahib olduğu bütün digər metodları, atributları
    #    verək bu OBJECTS variable-ına ki, bu variable vasitəsi ilə QUERYSET-in həmin metod və atributlarını çağıraraq istifadə edək. 

    #    Başqa cür deyəsi olsaq, MANAGER sözü idarə edən mənasına gəlir AS sözü isə 'KIMI' deməkdir. Yəni,  CartQueryset() klasını İdarəçi kimi OBJECTS variable-ına veririk. Yəni, CartQueryset() klasını OBJECTS variable-ı
    #    adı altında idarəçi kimi təyin edirik. Bu CartQueryset() klasıda QUERYSET klasını izlədiyi üçün belə bir zəncir yaratmış oluruq.  objects -> CartQueryset() -> QuerySet
    #    Və beləliklə QuerySet-in metod və atributları və özümüz yaradan CartQueryset() klasının içində yazacağımız digər metod və klaslar, OBJECTS variable-ı ilə bizim üçün əl çatan olur. 
    objects = CartQueryset.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
   
    def __str__(self):
        return f'Cart {self.user.username} | Product {self.product.name} | Quantity {self.quantity}'
    




    
