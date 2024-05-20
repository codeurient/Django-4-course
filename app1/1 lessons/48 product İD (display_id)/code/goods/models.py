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
    
    # 1) Şablonda hər məhsulun bir kodu olur. Məsələn: 000072, 1000156 və.s

    # 2) Biz hər məhsul əlavə etdikdə bu məhsulun bir identifikatoru yaranır: 1,2,3,4,5,6,7,8 ve.s

    # 3) Şablonda göstərmək istədiyimiz kod isə həmin bu identifikatordur. Ancaq ilk məhsulun İD-si 1 olduqda bu 1 ədədini kod kimi göstərə bilmərik. Bunun üçün
    # həmin İD-nin başına 00001 sıfırlar əlavə edirik. 

    # 4) Bunun ucun CLASS içində öz metodumuzu yaradırıq. Metodun adını: DİSPLAY_ID qoya bilərik (kim necə istəyir). Parametr olaraq SELF parametrini veririk. 
    # CLASS içində yaradilan DİSPLAY_İD funksiyasina verilmiş bu 'SELF' parametri həmin CLASS-ın özüdür. Funksiyanı 'goods/templates/goods/catalog.html' şablonu
    # içində çağırasıyıq. 
    def display_id(self):
        # 5) Funksiyamız STRİNG return edəcək. String-i 'F' açar sözü ilə yazırırq. Çünki F simvolu ilə aşağıda gördüyümüz kimi SPESİFİKATOR istifadə etmək olur.
        # 6) Bu spesifikatorun mənası 5 rəqəmli ədəd olsun və ilk 4ü (dördü) sıfırlar ilə başlasın deməkdir. 
        return f"{self.id:05}"
    
        #* 7) İndi şablona 'goods/templates/goods/catalog.html' gedərək funksiyamızı çağıraq:           <p class="product_id">id: {{ product.display_id }}</p>