from django.http import JsonResponse
from django.template.loader import render_to_string
# 1) Reverse funksiyasini IMPORT edirik. 
from django.urls import reverse
from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products



def cart_add(request):
    product_id = request.POST.get('product_id')
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
    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string("carts/includes/included_cart.html", {'carts': user_cart}, request=request)

    response_data = {
        "message": "Product added to cart",
        'cart_items_html': cart_items_html,
    }
    return JsonResponse(response_data)



def cart_change(request):
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')

    cart = Cart.objects.get(id=cart_id)
    cart.quantity = quantity
    cart.save()
    # 2) AJAX kodlarının yazılı olduğu JQUERY faylına səbətdəki məhsul miqdarını göndərmək üçün UPDATED_QUANTİTY adında variable yaradırıq və aşağıda RESPONSE_DATA içində göndəririrk. 
    updated_quantity = cart.quantity

    # 3) CART variable adını USER_CART ilə dəyişdirdik. 
    user_cart = get_user_carts(request)
    # 4) Kodun bu `{"carts": user_cart}`  hissəsini aşağıdakı RENDER_TO_STRING() funksiyasına daxil etmişdik. Sonrada ORDERS adlı xassə əlavə edəcəyimiz üçün CONTEXT adlı variable yaradaraq onun içinə yerləşdirdik. 
    context = {"carts": user_cart}

    # 5) request.META.get('HTTP_REFERER')   - Bu kod ilə, istifadəçinin hal-hazırda olduğu səhifəyə gəlmədən əvvəl olduğu səhifənin URL-sini əldə etmək üçündür.   Elde edilen URL-ni REFERER adlı variable içinə qoyuruq. Sonra REVERSE() funksiyası ilə `orders:create_order` bu string-i
    #    URL linkine çevirik və İF soröusu ilə həmin URL-nin REFERER variable-ındakı URL olub olmadığını yoxlayırıq. Əgər deyilsə İF heçnə etmir. İF o vaxt TRUE verəcək ki, gəldiyimiz səhifə SİFARİŞ səhifəsi olsun. 
    #    İF true olduqda CONTEXT variable-ına əlavə edilir ORDER adlı xassə və TRUE dəyəri.  Bu ORDER xassəsini İNCLUDED_CART.HTML faylında istifadə edirik. Çünki   `http://127.0.0.1:8000/orders/create_order/`    linkinə daxil olduqda CHECKOUT düyməsini gizlətmək lazımdır. 
    referer = request.META.get('HTTP_REFERER')
    if reverse('orders:create_order') in referer:
        context["order"] = True
    # 6) 
    cart_items_html = render_to_string("carts/includes/included_cart.html", context, request=request)

    response_data = {
        "message": "Quantity updated",
        'cart_items_html': cart_items_html,
        # 7) 
        "quantity": updated_quantity,
    }
    return JsonResponse(response_data)




def cart_remove(request):
    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id) 
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)

    # 8) yuxaridaki CART_CHANGE metodundan yazdiqlarimizin eynisini burda da yaziriq. 
    context = {"carts": user_cart}
    referer = request.META.get('HTTP_REFERER')
    if reverse('orders:create_order') in referer:
        context["order"] = True

    cart_items_html = render_to_string("carts/includes/included_cart.html", context, request=request)

    response_data = {
        "message": "Product deleted",
        'cart_items_html': cart_items_html,
        'quantity_deleted': quantity,
    }
    return JsonResponse(response_data)

