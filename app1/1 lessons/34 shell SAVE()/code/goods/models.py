from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'               
        verbose_name = 'Category'           
        verbose_name_plural = 'Categories'  




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


# 1) Django-nun terminal penceresine kecdikden sonra CATEGORIES adli CLASS-i terminala IMPORT etmek lazimdir:     'from goods.models import Categories'       yəni good qovlugu models faylindan
# Import etdikden sonra CATEGORIES class-i vasitesi ile cedveli idare ede bilerik:
#! 
# >>>   from goods.models import Categories             - import etdik
# >>>   x = Categories()                                - class-i 'x' deyiskenine verdik
# >>>   x.name = 'Office'                               - class-dan 'name' deyiskenini cagirdiq ve 'Office' deyilen deyer teyin etdik
# >>>   x                                               - neticeni gormek ucun 'x' deyiskenini cagirdiq
#* <Categories: Categories object (None)>               - netice yoxdur. Cunki SAVE() etmemisik.
# >>>   x.save()                                        - save() edirik
# >>>   x                                               - neticeni gormek ucun tekrar 'x' deyiskenini cagirdiq
# <Categories: Categories object (1)>                   - netice var. DB-e baxsaq gorerik ki, 'NAME' adli sütunda 'Office' yazir.
# >>>   x.slug = 'ofice'                                - eynisini 'slug' ucun edirik
# >>>   x.save()                                        - save() edirik
# >>>   x                                               - 'x' deyiskenini cagirdiq
#* <Categories: Categories object (1)>                  - netice var
# >>> 

# 2) Bu qaydadan DB-e melumat yazmaq ucun nadir hallarda istifade edilir. Normalda Controller klaslarinda edeceyik bu işləri. 

# 3) Terminalda cixmaq ucun yaziriq:   quit()