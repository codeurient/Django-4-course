from django.db import models

# 1) 37 nomreli dersde Admin panelə CATEGORY elave etdikde nə üçün 'Categories object (3)' deyə bir yazı gördüyümüzü başa düşmək üçün BASE.PY faylına baxaq. 590-cı sətr.
# 2) Bu faylı açmaq üçün aşağıda gördüyümüz MODEL sözünə klikləyirik. Öncə CTRL düyməsini basırıq sonra MOUSE-u klikləyirik. 
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