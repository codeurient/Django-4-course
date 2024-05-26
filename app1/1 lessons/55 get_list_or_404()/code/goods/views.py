from django.shortcuts import get_list_or_404, render
from goods.models import Products

def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        # 1) 7 CATEGORY var. 6-sında PRODUCT mövcuddursa və əgər 1-ində mövcud deyilsə şəkil 2-də olduğumu kimi qəribə bir görüntü əldə edirik. 
        # Ancaq səhifəyə daxil olduqda əgər PRODUCT mövcud deyilsə 'PAGE NOT FOUND (404)' deyə bir mesaj,  yaxud fərqli bir səhifə göstərə bilərik istifadəçilərə.
        # Bunun üçün ilk öncə həmin səhifənin mövcud olub olmadığını yoxlayan, GET_LİST_OR_404() adlı funksiyadan istifadə etməliyik. 
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug))

        # 2) Hələki səliqəsiz bir səhifə görəcəyik ekranda (şəkil 3). İndilik belə qalsın. Sonra bunu başqa səliqəli səhifə ilə necə əvəz edə biləcəyimizi görəcəyik.


    context = {
        "title": "Home - Catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)  

5

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)