from django.shortcuts import render
from goods.models import Products

# 1) 
def catalog(request, category_slug):
    # 2) Eger 'category_slug' beraber olarsa 'ALL' sozune onda DB-se sorgu gondererek butun PRODUCT-lari secirik. 
    if category_slug == 'all':
        goods = Products.objects.all()
    # 3) Eks halda FILTER() metodunda CATEGORY__SLUG xarici acarina CATEGORY_SLUG parametrindeki deyeri vererek demis oluruq ki, DB-dən hemin SLUG-a uygun gelen mehsulu bize ver.
    else:
        goods = Products.objects.filter(category__slug = category_slug)


    context = {
        "title": "Home - Catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)  




def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)    