from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'               
        verbose_name = 'Category'           
        verbose_name_plural = 'Categories'  
    
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
    
    def display_id(self):
        return f"{self.id:05}"
    
    # 1) Indi endirimlə bağlı olan hissəni edək. Endirim olduqda bir balaca fərqli informasiya göstəriləcəkdir. Bunun üçün ilk öncə bir metod yaratmalıyıq  
    # ki, endirimi hesablasın sonra isə İF-dən istifadə edərək endirim varsa 1ci infonu əks halda isə 2ci infonu göstərsin.
    def sell_price(self):
        # 2) self.discount  əgər 0 (sıfır) olsa bu FALSE deməkdir və funksiya aşağıda yazdığımız SELF.PRICE-ı return edəcək.
        if self.discount:
            # 3) Əgər DB-də DİSCOUNT sahəsinə hər hansısa dəyər əlavə etsək onda bu TRUE demək olacaq və İF işləyəcək. Meselen:  150 - 150 * 60 / 100 = 60 $
            return round( self.price - self.price * self.discount / 100,   2 )
        
        return self.price