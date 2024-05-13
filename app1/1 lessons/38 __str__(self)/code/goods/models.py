from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'               
        verbose_name = 'Category'           
        verbose_name_plural = 'Categories'  
    
    def __str__(self):
        # 1) SELF sözünün mənası ÖZ deməkdir və SELF dedikdə nəzərdə tutulan yuxarıda yaratmış olduğumuz CATEGORİES klasıdır. Yəni, SELF yazaraq həmin klass-ı çağırırıq. 
        # SELF.NAME isə həmin class-ın içindən NAME dəyişkənini çağırır. NAME dəyişkənidə MODEL-in yəni, TABLE-ın sütununun adıdır. Bu sütunada ADMİN paneldə 'All products' dəyərini verdik. 
        return self.name
    
    # 2) return self.name    yazdıqda       'Categories object (4)'     adının dəyişmə səbəbi DJANGO-nu yaradan proqramistlərin      '__str__'       metodunu həmin yazıya müraciət etmək üçün yaratmış olmalarıdır.
    




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

    # 3) Eynisini PRODUCTS üçündə yazaq.
    def __str__(self):
        return f'{self.name} Quantity: {self.quantity}'