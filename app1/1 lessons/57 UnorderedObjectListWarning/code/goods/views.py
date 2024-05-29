from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Products

def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(1) 


    context = {
        "title": "Home - Catalog",
        "goods": current_page,
    }
    return render(request, "goods/catalog.html", context)  

5

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)



#! 1)  56 nömrəli dərsdə Səhifəni yenilədikdə, TERMİNAL pəncərədə 'UnorderedObjectListWarning' deyə bir xəbərdarlıq mesajı görəcəyik. Bu xəbərdarlıq mesajını aradan qaldırmaq lazımdır. 

# Bu xəbərdarlıq mesajı deyir ki, PAGİNATOR bizə, dəqiq olmayan məlumatlar verə bilər çünki PRODUCT-ların başlanğıcda necə listələnəcyini yəni sıralanacağını (UNORDERED) bildirməmişik. 
# Və tələb edir ki, biz PRODUCT-ları tam dəqiq sıralayaq. 

# Bu xəbərdarlıq mesajını aradan qaldırmaq üçün MODEL-ə keçid edirik və yazırıq......... (  GOODS/MODELS.PY  )