from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Products


# 1) Artıq PAGE parametrinə ehtiyac yoxdur deyə onu silirik. Niyə silirik ? Çünki  GOODS/URLS.PY  faylındakı url marşrutuna ehtiyacımız yoxdur:        path('<slug:category_slug>/<int:page>/',         views.catalog, name='index'),
#    Dəyərləri GET sorğunun REQUEST parametri ilə verəcəyik. Marşrut olaraq isə ƏSAS marşrut olan bunu istifadə edəcəyik:                              path('<slug:category_slug>/',                    views.catalog, name='index'),

def catalog(request, category_slug):
    # 2) REQUEST parametrindən dəyərləri əldə etmək üçün PAGE adından variable yaradırıq. Sonra REQUEST parametrini ona veririk. Sonra DİCT-in adını yazırıq: GET.  Sonra ise GET() metodu ilə həmin dict içindən dəyəri əldə edirik.
    #    Əgər URL yerində PAGE adında açar olmazsa DEFAULT olaraq həmin açar söz yaradılacaq və dəyər olaraq 1 ədədi veriləcək:
    #                                                                                                                           <a class="page-link" href="?page={{ 1 }}">{{ 1 }}</a>
    page = request.GET.get('page', 1)
    # 3) İndi ŞABLON-a gedirik. 


    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug))

    paginator = Paginator(goods, 3)
    # 4) INT() metodu ile elde edilen deyerin REQEMSAL oldugunu bildirmeliyik.
    current_page = paginator.page(int(page)) 


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