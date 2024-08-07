from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products


# 1) CARTS / URLS.PY     faylından conventorları sildiyimiz üçün artıq burada da  PRODUCT_SLUG  parametrinə ehtiyacımız yoxdur deyə silirik.  
def cart_add(request):
    # 2) AJAX sorğunun POST metodu ilə göndərilən PRODUCT_İD-ni bu controllerin,  REQUEST parametri ilə əldə edirik.           
    product_id = request.POST.get('product_id')
    # 3) Sonra DB-dən məhsulu İD -sinə görə çağırırıq.
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts= Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    # 4) Burada     RETURN REDIRECT()     evezine yaziriq:
    # 5) RENDER_TO_STRİNG() metodu ilə şablonu stringə render edirik. 1ci parametrdə render ediləcək şablonumuz var. 2ci parametrdə bu şablona əlavə ediləcək obyektdir. USER_CART() bizim CARTS / TEMPLATETAGS / CARTS_TAGS.PY faylında
    #    yaratdığımız metodumuzdur. Həmin metod vasitəsi ilə istifadəçinin səbətindəki məhsulları əldə edirik. Həmin səbəti CARTS xassəsi adı altında İNCLUDED_CART.HTML faylına göndərmək üçün bəzi düzəltmələr etməliyik. 
    # 6) Bunun üçün CARTS qovluğunda     UTİLS.PY    faylında fayl yaradırıq.  Sonra CARTS_TAGS.PY faylındakı USER_CARTS() metodunun içində əvvəl yazdığımız kodları kəsərək götürürük və UTİLS.PY faylına yerləşdiririk. 
    #    Bu UTILS.PY faylinda yaratdigimiz     GET_USER_CARTS()     metodunu controllerdə istifadə edirik. Bu metod istifadəcənin səbətindəki məhsulları əldə etmək üçün istifadə edilir. 
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string("carts/includes/included_cart.html", {'carts': user_cart}, request=request)

    # 7) RESPONSE_DATA adlı dict yaradırıq və bu dict-ə 2 xassə yerləşdiririk: a) Notification üçün MESSAGES, b) CART_ITEMS_HTML-i, hansıki bu xassə yuxarıdakı İNCLUDED_CART.HTML faylındakı şablonu ehtiva edir. 
    response_data = {
        "messages": "Product added to cart",
        'cart_items_html': cart_items_html,
    }
    # 8) DICT formatını JSON formatına çevirerek RETURN edirik. 
    return JsonResponse(response_data)





def cart_change(request, product_slug):
    ...

def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])





