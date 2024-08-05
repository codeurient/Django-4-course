from django.shortcuts import redirect, render

from carts.models import Cart
from goods.models import Products

# 1) REQUEST        parametri ile http sorgusunun deyerlerini elde edirik:                          <WSGIRequest: GET '/cart/cart_add/tea-table-and-three-chairs/'>
#    PRODUCT_SLUG   parametri ile http sorgusundan gelen PRODUCT-un SLUG deyerini elde edirik       product_slug='tea-table-and-three-chairs'    

# 2) OBJECTS, Django model class-larinda default olarak təyin edilən bir yönəticidir (manager). Bu yönətici istifadə edilərək DB sorguları yaratmaq mümkündür.  
def cart_add(request, product_slug):
    # 3) DB-də, PRODUCTS cədvəlində SLUG sütunu vardır. Həmin SLUG sütununda olan dəyərləri PRODUCT_SLUG parametri ilə əldə etdiyimiz dəyərlər ilə eyniləşdirərək uyğun gələn məhsulu əldə edirik. 
    #    PRODUCT variable-ı içində məhsulun adı, qiyməti, endirimli qiyməti, hansı kateqoriyə aid olduğu, id-si və.s məlumatlar mövcuddur.
    product = Products.objects.get(slug=product_slug)

    # 4) Əgər istifadəçi sayta giriş edərək səbət ikonunu kliklərsə onda     'request.user.is_authenticated'       TRUE verəcək əks halda FALSE verəcək.
    if request.user.is_authenticated:
        # 5) Sayta giriş edən istifadəçinin səbətə əlavə etdiyi məhsulları əldə edərək    'carts'     variable-ına veririk. Filter() metodunun içində hansı məhsulu və hansı istifadəçinin məhsulunu
        #    əldə etmək istədiyimizi bildirmişik. Filter() metodundan olan USER və PRODUCT parametrləri CARTS modelində olan sütunların adlarıdır. Təbii ki, ilk öncə səbət boş olacaq. Səbət boşdusa
        #    CARTS variable-ında heçnə yoxdur. Heçnə yoxdursa FALSE əgər məhsul varsa TRUE əldə edirik. 
        carts= Cart.objects.filter(user=request.user, product=product)

        # 6) CARTS variable-ında məhsulun olub olmadığını EXİSTS() metodu ilə yoxlayırıq. Elə yuxarıda yazdığımı FİLTER()-də onun üçün lazım idiki, əgər artıq səbətdə məhsul varsa bunu yoxlayaq və üstünə
        #    yenisini əlavə edək. 
        if carts.exists():
            # 7) Əgər səbət boş deyilsə CART adında variable yaradaraq FİRST() metodu ilə ilk məhsulu əldə edirik və həmin variable içinə bu məhsulu qoyuruq
            cart = carts.first()
            # 8) Əgər məhsul varsa onda bu məhsulun QUANTİTY sütununun dəyərini +1 artırırıq
            if cart:
                cart.quantity += 1
                # 9) Mövcud məhsulun sayını artırdıqdan sonra isə onu SAVE() edirik
                cart.save()
        else:
            # 10) Əgər DB-də EXİSTS() deyilsə məhsul yəni yoxdursa onda həmin məhsulu CREATE() edirik. Yəni yaradırıq DB-də. CART cədvəlinin USER sütununa məhsulu əlavə edən istifadəçinin İD-sini qoyuruq, 
            #     PRODUCT sütununa məhsulun SLUG adını qoyuruq. QUANTİTY sütununa isə 1 sayınısını qoyuruq və əgər ikinci eyni məhsul əlavə edilsə yuxarıda olduğu kimi +1 artırırıq.
            Cart.objects.create(user=request.user, product=product, quantity=1)
    
    # 11) Səbət ikonuna basaraq məhsulu səbətə əlavə etdikdən sonra hal-hazırda olduğumuz səhifəyə geri qayıtmaq üçün isə, REDİRECT() metodundan istifadə edirik. Hansı səhifədə olsaqda o səhifəyə geri 
    #     qayıdasıyıq. Bunun üçün REQUEST sorğusunun META paramettrinin HTTP_REFERER adlı açar sözündən istifadə edirik. 
    return redirect(request.META['HTTP_REFERER'])




def cart_change(request, product_slug):
    ...

def cart_remove(request, product_slug):
    ...


