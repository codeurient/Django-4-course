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
        "slug_url" : category_slug,
    }
    return render(request, "goods/catalog.html", context)  



def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)


# 1) Proqrami işə saldıqdan sonra sayta gedirik və manual olaraq belə bir URL yazaraq ENTER düyməsini basırıq:          http://127.0.0.1:8000/catalog/all/?page=2&q=table

# 2) Sonra yenidən VScode platformasına qayıdaraq həmin bu GOODS/VIEWS.PY faylındakı CATALOG() metodunun içindəki REQUEST parametrinin üzərinə kursoru gətirərək onun əldə etdiyi cavaba baxırıq: 
#                                                                                                                                                                                                GET <QueryDict: {'page': ['2'], 'q': ['table']}>

# Bu bir DICT-dir ve icinde bizim manul olaraq daxil etdiyimiz ACAR ve DEYERLER movcuddur. Bu o demekdir ki, CONTROLLER-de biz hemin DEYERLERI request parametri vasitesi ile elde ede bilerik.


# 3) Bu qeder. Artiq DEBUG rejimi dayandiraq ve deyerleri elde edek. 