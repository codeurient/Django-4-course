from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'               
        verbose_name = 'Category'           
        verbose_name_plural = 'Categories' 
        ordering = ("id", )

    
    def __str__(self):
        return self.name




class Products(models.Model):
    name        = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug        = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    image       = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Images') 
    price       = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Price')  
    discount    = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Discount with %') 
    quantity    = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    category    = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Category') 

    class Meta: 
        db_table = 'product'               
        verbose_name = 'Product'           
        verbose_name_plural = 'Products'


    def __str__(self):
        return f'{self.name} Quantity: {self.quantity}'
    
    # 1) ADMİN PANEL-də hər hansısa bir məhsulu açdıqda yəni PRODUCTS sehifesinde birdən çox məhsul var və biz sadəcə birinə daxil oluruq:   http://127.0.0.1:8000/admin/goods/products/12/change/
    #    Həmin səhifədə sağ tərəfdə elə bir düymə yarada bilərik ki, məsələn məhsulu əlavə etdikdən sonra bu düyməni klikləyərək veb səhifəyə daxil olaq və məhsulun necə göründüyünə baxaq. 
    #    Bunun üçün hər MODEL içində   Get_Absolute_Url()     adında DJANGO-nun daxili, metodu vardır və URL marşrutlar yaratmaq üçün istifadə edilir. 
    #    Bu metod ADMIN PANEL ucun avtomatik olaraq cagrilir ve sag terefde duyme yaradir. Ancaq aşağıdakı    SELL_PRİCE()     kimi şablonda da çağıraraq istifadə etmək mümkündür. 
    def get_absolute_url(self):
        # 2) REVERSE() metodu  hansı URL-ni yaradaraq bu URL ilə iş görəcəyimizi bildirir. KWAGRS parametri ilə bu URL-nin conventor-unun nə olduğunu bildiririk. SELF.SLUG isə bu conventor-un 
        #    hansı dəyərdə olacağını bildirir. Bunlar hamısı birləşərək bir bütün marşrut əmələ gətirir:    http://127.0.0.1:8000/catalog/product/iphone-13
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
        # 3) Qısaca   Get_Absolute_Url()   metodu avtomatik çağrılaraq   REVERSE()  metodu ilə təyin edilən URL-də  VEB səhifəyə keçid etmək üçün lazım olan düyməni formalaşdırır. 
    
    

    def display_id(self):
        return f"{self.id:05}"
    
    
    def sell_price(self):
        if self.discount:
            return round( self.price - self.price * self.discount / 100,   2 )
        
        return self.price
    



    

