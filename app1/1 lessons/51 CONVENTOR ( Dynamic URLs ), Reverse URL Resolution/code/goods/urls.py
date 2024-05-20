# 1) URL adresleri 2 hisseye ayrilir:
#                                    a) Static:  əlnən manual daxil etdiklerimiz 
#                                    b) Dynamic: özü dəyişən

# Məsələn yuxarıda bir LİST var ve içində 2 dənə URL adres görürük. 1cisi Mehsullar sehifesi, 2cisi Deqiq bir mehsul ucun ayrilan sehifedir.
# NOT: path() metonun 1ci parametrinde eslinde 'catalog' sozu var sadece bu hisse APP/URLS.PY faylinda oldugu ucun burda gormuruk hemin CATALOG sozunu.  

# Brauzerde bu cur yazdiqda 'http://127.0.0.1:8000/catalog'           butun mehsulları görürük.  
# Brauzerde bu cur yazdiqda 'http://127.0.0.1:8000/catalog/product'   sadece seçmiş olduğumuz dəqiq bir məhsulu görürük.

# Bizdə cəmi 7 Category var. Bu 7 fərqli səhifə deməkdir. Həmin səhifələrə daxil olmaq üçün istifadə edəcəyimiz URL adresləri bu cür ola bilər:
# http://127.0.0.1:8000/catalog                 
# http://127.0.0.1:8000/catalog/kitchen
# http://127.0.0.1:8000/catalog/bedroom
# http://127.0.0.1:8000/catalog/livingroom
# http://127.0.0.1:8000/catalog/office
# http://127.0.0.1:8000/catalog/accossories
# http://127.0.0.1:8000/catalog/decor ve.s 

# Indi 70 Category olmuş olsa idi hər dəfə manul URL adres əlavə etmək doğru olardımı? Yaxud ticarət saytımızda 50 000 məhsul olduqda hər məhsul üçün bir URL mi yaratmaq lazım gələcək: 
                                                                                       # http://127.0.0.1:8000/catalog/kitchen/1
                                                                                       # http://127.0.0.1:8000/catalog/kitchen/2
                                                                                       # http://127.0.0.1:8000/catalog/kitchen/3
                                                                                       # http://127.0.0.1:8000/catalog/kitchen/4 ve.s.........  Xeyr !!!
# Xeyr. Deməli elə etməliyik ki bəzi URL adresiləri, Dynamic formada əlavə edilsin. 

# 2) Elə bunun üçün CONVENTOR (<int:year>) deyilən bir sistem mövcuddur:  
#  https://docs.djangoproject.com/en/5.0/topics/http/urls/
                                                            # urlpatterns = [
                                                            #     path("articles/2003/"                                     , views.special_case_2003),
                                                            #     path("articles/<int:year>/"                               , views.year_archive),
                                                            #     path("articles/<int:year>/<int:month>/"                   , views.month_archive),
                                                            #     path("articles/<int:year>/<int:month>/<slug:slug>/"       , views.article_detail),
                                                            # ]
                                    

from django.urls import path
from goods import views
app_name = 'goods'

urlpatterns = [
    path('',         views.catalog, name='index'),

    path('product/<int:product_id>/', views.product, name='product'),
    # 3) Conventor-lar imkan yaradir ki, URL bolmesinde yazili olan balaca fragmentleri elde edek. Elde etdiyimiz fragmentleri ise gonderirik CONTROLLER-lere (parametr vasitesi ile elde edirik fragmenti).
    # MARŞRUTA adından istifadə edərək, Controller-də yazdığımız kod ilə DB-dən həmin MARŞRUTA uyğun gələn məlumatları əldə edirik. Sonra isə Şablonda həmin məlumatları əks etdiririk. 
]

# 4) Conventor-lar, çeşit olaraq bir neçə dənədir:   str,      int,      slug,      uuid,      path
# Marşrutumuzu yaradırıq: 'product/<int:product_id>/'         _______________________________________Sonra Controllerə gedərək eyni bu adda parametr təyin edirik:  product_id