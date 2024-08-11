from django.db import models
from goods.models import Products
from users.models import User

class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self: 
            return sum(cart.quantity for cart in self)
        return 0



class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User") 
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name="Product")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Quantity")
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Created date")

    class Meta:
        db_table = "cart" 
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    objects = CartQueryset.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
   
    def __str__(self):
        # 1) 104 nomreli dersde sebete anonim olaraq mehsul elave etdikde Admin panelde xeta mesaji alirdiq cunki istifadeci yoxdursa USERNAME null olurdu. Bunun ucunde xeta mesaji alirdiq.
        #    Buna gore de, şərt qoşaraq deyirik ki, əgər USER varsa nəticə qayıtsın əks halda USER olmadan qayıtsın nəticə. 
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'
                
        return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'
    


    