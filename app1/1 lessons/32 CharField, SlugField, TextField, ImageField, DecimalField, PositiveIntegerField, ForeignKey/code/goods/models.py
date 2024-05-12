from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'               
        verbose_name = 'Category'           
        verbose_name_plural = 'Categories'  




class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    # 1) ImageField() metodunun 'upload_to' adlı parametri şəkilləri hara yükləmək lazım olduğunu bildirir. Binar faylları DB-də yadda saxlamaq olar 
    # ancaq, bu nadir hallarda edilir ve en yaxşısı odur ki, bu cür faylları saytımızın Serverində yaxud tamam fərqli bir Serverdə yadda saxlayaq.
    # 'upload_to' parametrində şəklin özü yox həmin şəklin yolunu göstərən link qeyd edilir. Hal-hazırda şəkilləri yadda saxlayacaq bir Serverimiz olmadığı üçün
    # proqramimizin icinde MEDIA adinda qovluq yaradiriq ve sekilleri bu qovluga yerlesdiririk. 
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Images') 
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Price') # 2) DecimalField - bu metod kesir ededler elave etmek ucundur. 
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Discount with %') 
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    # 3) Indi demeliyik ki, bu mehsul yəni PRODUCT hansı CATEGORY-e aiddir ?! Yəni, Xarici Açar (foreginKey) vasitesi ile 2 ferqli cedveli bir-birine baglamaliyiq.
    # ForeignKey() metodundan, PRODUCTS cedvelindeki mueyyen sütun ile CATEGORIES cedvelindeki müəyyən sütunu bir-birinə bağlamaq üçün istifadə edirik. Ve bu sayedə
    # CATEGORY variable-ında olan dəyərdən istifadə edərək, DİGƏR cədvəldəki dəyərləri çağıra bilərik. 
    #       a) Bu metodun 1ci parametri 'TO' hansı Table ilə əlaqə yaradacağımızı göstərir. 
    #       b) Bu metodun 2ci parametri 'ON_DELETE' onu bildirir ki, proqram, müəyyən kateqoriyaya bağlı produktlar ilə nə edəcək əgər həmin kateqoriya silinərsə?¡
    #
    #          I) Proqram həmin kateqoriya ilə əlaqəli bütün produktları silsin.    II) Boş sahəyə default olaraq bir dəyər təyin etsin.    III) Produkt olduğu müddətcə kateqoriya silinə bilməsin
    #                                     CASCADE                                                           SET_DEFAULT                                                PROTECT
    #
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Category')  # 4) Indi novbe cedveli qeydiyyata almaqdadir. Bunun ucun GOODS/ADMIN.PY faylina gedirik.

    class Meta: 
        db_table = 'product'               
        verbose_name = 'Product'           
        verbose_name_plural = 'Products'  