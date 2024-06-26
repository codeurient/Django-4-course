from django.shortcuts import render

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        "title": "Home - Catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)  




# 1) Controller-de de parametri 'product_slug' olaraq deyisdiririk. 
def product(request, product_slug):
    # 2) GET() sorgunuda SLUG uzre edirik.
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, "goods/product.html", context=context)    