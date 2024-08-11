from django.contrib import admin
from goods.models import Categories, Products



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # 1) Tekrar xatirlatma edim ki, prepopulated_fields onun ucun lazimdir ki, NAME-den asili olaraq SLUG avtomatik olaraq yaransin.
    prepopulated_fields = { 'slug' : ('name',) }    
    # 8) KATEQORİLƏRİ adları ilə sıralamaq üçün LİST__DİSPLAY variable-ından istifadə edirik. 
    list_display = ['name', ]




@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('name',) }
    # 2) LIST_DISPLAY adında bir daxili LİST yaxud DİCT yaradiriq. Bu variable-dan, ADMIN PANEL-də PRODUCT olan yerdə sadəcə məhsulun adını yox məhsulun qiymətini, miqdarını və.s göstər demək üçün istifadə edilir. 
    #    Həmin adları PRODUCT MODEL-ində olduğu kimi yazmalıyıq. 
    list_display = ['name', 'quantity', 'price', 'discount']

    # 3) Elə etmək olarkı məsələn DİSCOUNT-u dəyişmək üçün məhsulun adına basaraq keçilən səhifədə yox elə bir başa həmin sahənin dəyərini olduğumuz sihəfədə dəyişdirək. Bunun ucun LİST_EDİTABLE -dən istifadə edirik.
    list_editable = ['discount']

    # 4) Eger birden cox mehsul varsa SEARCH sahesi elave ederek NAME uzre axtaris et deye bilerik.
    search_fields = ['name']

    # 5) Filtir sistemi yaratmaq ucun LIST_FILTER variable-indan istifade edirik.
    list_filter = ['discount', 'quantity', 'category']


    # 6) PRODUCT list-inden her hansisa xüsusi bir mehsulu secerek sehifeye daxil oluruq ve burada sahelerin düzülüş qaydasını təyin edə bilərik. Yaxud gizlədə bilərik. Bunun üçün FİELDS variable-ından istifade edirik.
    fields = [
            'name', 
            'category', 
            'slug', 
            'description', 
            'image', 
            ('price', 'discount'), # 7) PRICE ve DISCOUNT yan-yana olacaq.
            'quantity', 
        ]
    
