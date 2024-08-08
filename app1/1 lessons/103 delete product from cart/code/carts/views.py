from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

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
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string("carts/includes/included_cart.html", {'carts': user_cart}, request=request)

    response_data = {
        "message": "Product added to cart",
        'cart_items_html': cart_items_html,
    }
    return JsonResponse(response_data)





def cart_change(request, product_slug):
    ...

def cart_remove(request):
# 1) AJAX ilə göndərilən səbətdəki məhsulun İD-sini alırıq. Bu İD ilk öncə İNCLUDED_CART.HTML faylından JQUERY-AJAX.JS faylına göndərilir sonra isə ordan bura.  
    cart_id = request.POST.get('cart_id')
# 2) Sebetdeki bir mehsulu ID-sine gore elde edirik.
    cart = Cart.objects.get(id=cart_id) 
# 3) CART cedvelinden QUANTITY sutunu ile hemin sutunda olan bir mehsullun sayini elde edirik. 
    quantity = cart.quantity
# 4) Sebete elave edilen mehsulu silirik.
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string("carts/includes/included_cart.html", {'carts': user_cart}, request=request)

    response_data = {
        "message": "Product deleted",
        'cart_items_html': cart_items_html,
        'quantity_deleted': quantity,
    }
    return JsonResponse(response_data)

