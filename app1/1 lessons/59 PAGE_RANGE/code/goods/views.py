from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Products


def catalog(request, category_slug, page = 1):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page) 


    context = {
        "title": "Home - Catalog",
        "goods": current_page,
        #! 1) SLUG_URL xassesine CATEGORY_SLUG-ın dəyərini verərək, GOODS - TEMPLATES - GOODS - CATALOG.PY  şablonuna göndəririk ki, belə olsun:  
        #!                                                                                                                                       <a  href="{% url "catalog:index" slug_url page %}">  ...  </a>
        #!                                                                                                                                       <a  href="http://127.0.0.1:8000/catalog/all/1     >  ...  </a>
        "slug_url" : category_slug,
    }
    return render(request, "goods/catalog.html", context)  

5

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)