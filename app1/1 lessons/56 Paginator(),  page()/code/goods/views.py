from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Products

def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug))

    # 1) 'PAGINATOR' adında variable yaradaraq ona, PAGİNATOR() funksiyasını veririk. Bu funksiya 2 parametr qəbul edir:
    #                                                                                                                    a) QuerySet - hal hazirda GOODS variable-ı
    #                                                                                                                    b) Say      - meselen 3 (sehifede nece mehsul gosterilsin demekdir)
    paginator = Paginator(goods, 3)

    # 2) PAGİNATOR() funksiyasi ilə PRODUCT-ların neçə-neçə göstəriləcəyini yazdıqdan sonra bir variable daha yaradırıq: CURRENT_PAGE və PAGE() metodu ilə hər səhifədə göstəriləcək PRODUCT-u əldə edirik. Bu metodda yazdığımız 
    # 1 ədədi onu bildiririk, 1ci səhifədə 3 məhsulu göstər. Həmin ədədi 2 etsək onda 2ci səhifədə göstəriləcək digər 3 məhsulu əldə edəcəyik. 
    current_page = paginator.page(1) #! Hələki bu ədədi manual olaraq dəyişə və fərqli nəticəni görə bilərik.


    context = {
        "title": "Home - Catalog",
        # 3) Artıq GOODS əvəzinə CURRENT_PAGE variable-ını ŞABLON-a göndəririk. Həmin CURRENT_PAGE əslində GOODS variable ilə eynidir. Sadəcə LİMİT-li məhsul sayı mövcuddur.
        "goods": current_page,
    }
    return render(request, "goods/catalog.html", context)  



def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)



#! https://docs.djangoproject.com/en/5.0/topics/pagination/


#!     http://127.0.0.1:8000/catalog/decor/