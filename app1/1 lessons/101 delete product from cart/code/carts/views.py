from django.shortcuts import redirect, render

from carts.models import Cart
from goods.models import Products

def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts= Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    
    return redirect(request.META['HTTP_REFERER'])




def cart_change(request, product_slug):
    ...

# 1) Ikinci parametr olaraq CART_ID yaziriq. Yəni, CART cədvəlinin İD-sini əldə edirik. 
# 2) Bu parametrin elde etdiyi deyeri INCLUDED_CART.HTML şablonundan göndəririk. 
def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])


