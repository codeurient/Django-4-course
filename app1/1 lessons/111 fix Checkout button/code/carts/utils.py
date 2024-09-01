from carts.models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        # 1) SELECT_RELATED()   metodu, DJango ORM sistemində, sorğuları optimizasiya etmək üçün istifadə edilir. Bu qayda ilə bir-biri ilə əlaqəli olan modellər birlikdə bir
        #    sorğu həyata keçirir. Məsələn, CART modelinin bir     ForeignKey    sütunu olan PRODUCT  modeli  vardır və CART  modelinə hər dəfə sorğu göndərdikdə bununla əlaqədə 
        #    olan   PRODUCT   modelinədə sorğu göndərilir. Buda performans itkisinə səbəb olur. Bunun üçün SELECT_RELATED() metodu ilə əlaqəli cədvəllər birləşdirilərək tək sorğu yaradılır.
        return Cart.objects.filter(user=request.user).select_related('product')
    
    if not request.session.session_key:
        request.session.create()
        # 2) SELECT_RELATED()
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product')


# 3) Səhifəni yeniləyərək sorğuya bir daha göz gəzdirdikdə aşağıdakı forma bir sorğu yarandığını görəcəyik

#!   SELECT ••• FROM "cart" INNER JOIN "product" ON ("cart"."product_id" = "product"."id") WHERE "cart"."user_id" = 5