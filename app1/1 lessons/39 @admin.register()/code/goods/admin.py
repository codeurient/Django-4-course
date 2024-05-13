from django.contrib import admin
from goods.models import Categories, Products

# 1) SLUG sütunu avtomatik olaraq doldurulan sütundur. Yəni, manul şəkildə İNPUT sahəsinə özümüz nəsə yazaraq doldurmuruq. 
# Bunun üçün bir neçə yol vardır. Biz ən sadə və ən çox tərcih edilən yolu nəzərdən keçirək. GOODS/ADMIN.PY faylinda CLASS-larimizi REGISTER() 
# metodu istifadə edərək qeydiyyatda almışıq. Bu cür metod bizə icazə verimir ki, hər hansısa dəyişiklik edək. Buna görə həmin metodu ilk öncə kommentə alırıq.

# admin.site.register(Categories)
# admin.site.register(Products)



# 2) Sonra isə REGİSTER() dekoratoru vasitesi ile CATEGORİES modelini ADMİN panelinde gostermek ucun qeydiyyata aliriq. 
# Və aşağıda CategoriesAdmin adında öz CLASS-ımızı yaradaraq hansı SAHƏNİN (sütunun) avtomatik dolduruması gərəkdiyini kodluyuruq.  
@admin.register(Categories)
# 3) Bu CLASS içində, yazacagimiz kodlar sayəsində, yazılarımızı daha detallı daha ətraflı şəkildə, ADMİN panildə göstərə bilərik.  
class CategoriesAdmin(admin.ModelAdmin):
    # 4) 'prepopulated_fields'  - bu variable-a, Automatik doldurulacaq sahələri (sütunları) veririk. 1ci olaraq DİCT təyin edirik, sonra avtomatik doldurulacaq
    # sahənin (sütunun) adını yazırıq. 2ci olaraq [] (list) yaxud () (tuple) veririk. Həmin TUPLE içində STRİNG formatında 'NAME' sahəsinin (sütunun) adını 
    # yazasıyıq. Bu o deməkdir ki, yəni SLUG sahəsinə (sütununa) avtomatik veriləcək dəyər NAME sahəsindən (sütunundan) gəlsin. NOT: name olmasə şərt deyil. 
    prepopulated_fields = { 'slug' : ('name',) }

    # 5) NAME sahəsinə bir şeylər yazdıqda SLUG sahəsi avto doldurulur ancaq istəsək sahəni təmizləyərək öz sözlərimizi yaza bilərik.





# 6) Eynisini Products ucun edirik.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }





#! MODELLER daha doğru şəkildə yuxarıdakı kimi qeydiyyata alınır.  