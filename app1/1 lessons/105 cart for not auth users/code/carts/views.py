from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products




def cart_add(request):
    product_id = request.POST.get('product_id')
    product = Products.objects.get(id=product_id)

    # 1) Bu kod əgər USER giris edibdirsə məhsulun səbətə əlavə edilməsini yoxlayır. Aşağıda isə ELSE ilə giriş etməyibdirsə SESSİON KEY yaradırıq və məhsulu session-larda tuturuq.
    if request.user.is_authenticated:
        carts= Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    # 2) CART cedvelinde SESSİON_KEY və PRODUCT sütunları var və bu sütunda 'request.session.session_key' yəni unikal açar və 'product' yəni uyğun gələn məhsul varsa həmin məhsulu CARTS adlı variable-a qoyuruq.
    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
        # 3) Sorgu ile bu CARTS variable-sinde mehsulun olub olmadigini yoxlayiriq ve eger varsa +1 artir deyirik
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        # 4) Eks halda ise yəni mehsul yoxdursa onu yaradiriq.  Ancaq bizde hal-hazirda session-key yoxdur. Bunun üçün istifadeci sayta daxil olan kimi ona session key vermek lazimdir. Daxil oluruq UTİLS.PY faylına. 
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

    cart = get_user_carts(request)
    cart_items_html = render_to_string("carts/includes/included_cart.html", {'carts': cart}, request=request) 

    response_data = {
        "message": "Quantity updated",
        'cart_items_html': cart_items_html,
    }
    return JsonResponse(response_data)





def cart_remove(request):
    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id) 
    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string("carts/includes/included_cart.html", {'carts': user_cart}, request=request)

    response_data = {
        "message": "Product deleted",
        'cart_items_html': cart_items_html,
        'quantity_deleted': quantity,
    }
    return JsonResponse(response_data)

