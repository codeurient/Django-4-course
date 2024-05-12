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


# 1) pip install ipython      - interaktiv python yukleyirik. Nedir bu IPYTON ? Normal terminalda isleyende auto complete baş vermir. Bunun ucun terminal ile 
#                               daha effektli islemek ucun bele bir kitabxana yukleyirik. TAB duymesini basdiqda bize işarəler verir ki, neleri istifade ede bilerik ve.s.

# 2) ipython                  - bu cur terminalda yazaraq kitabxanani işə salırıq. Yaxud eger 'İPYTHON' yuludurse 'PYTHON MANAGE.PY SHELL' yazsaq bele avtomatik olaraq 'IPYTHON' açılacaq.