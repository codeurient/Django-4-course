from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Products


# 1) Aşağıda nömrə 2 yazan yerdə, səhifələri MANUL  'PAGE(1)'  olaraq daxil etmişdik.   Ancaq indi elə etməliyik ki, Şablonda 1,2,3,4 və.s kliklədikdə özü avtomatik dəyişsin. Bunun üçün 1 parametr
#    əlavə edirik və default olaraq 1 veririk ki, başlanğıc olaraq hər zaman 1ci səhifə göstərilsin______ Məsələn: page = 1_______ 

# 2) Sonra GOODS/URLS.PY  faylında yeni marşrut yaradırıq. Bu marşrut da, belə yazacağıq:     path('<slug:category_slug>/<int:page>/',         views.catalog, name='index'),     
#    Bu marşrutda yazmış olduğumuz PAGE parametri bizim URL yerində yazdığımız ƏDƏD-ləri əldə edir     http://127.0.0.1:8000/catalog/all/2     və GOODS/VIEWS.PY controllerində ki, PAGE parametrinə ötürür:       
def catalog(request, category_slug, page = 1):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug))

    paginator = Paginator(goods, 3)
    #! 2) 
    current_page = paginator.page(page) 


    context = {
        "title": "Home - Catalog",
        "goods": current_page,
    }
    return render(request, "goods/catalog.html", context)  



def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)