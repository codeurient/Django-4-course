from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Products
# 3) Q_SEARCH() funksiyasini istifade ede bilmek ucun UTILS.PY faylini IMPORT edirik.
from goods.utils import q_search

# 4) category_slug parametrinə DEFAULT olaraq NONE dəyərini veririk ki, əgər SLUG üzrə axtarış yoxdursa xəta almayaq və aşağıda yazmış olduğumuz İF yox ELİF ilə axtarış edilsin. 
def catalog(request, category_slug = None):
    page     = request.GET.get('page'    , 1)
    on_sale  = request.GET.get('on_sale' , None)
    order_by = request.GET.get('order_by', None)
    query    = request.GET.get('q'       , None)
    # 1) Controller də qarşı tərəfdən yəni MAİN/TEMPLATES/MAIN/BASE.HTML-dən göndərilən SEARCH sahəsinin dəyərini 'request.GET.get('q', None)' metodu ilə əldə edirik və 'QUERY' adlı variable-a yerləşdiririk. 

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        # 2) SEARCH ile məhsullarə FILTER-ləmək üçün çox kod yazmaq lazım gəldiyindən, kodları başqa bir fayl içində yazaraq həmin faylı VIEWS.PY faylına İMPORT etmək daha məsləhətə uyğundur. Bunun üçün ilk öncə GOODS/UTILS.PY adında başqa
        #    bir fayl yaradırıq. Bu faylın içində Q_SEARCH(query) adlı bir funksiyamız olacaq və 'QUERY' parametrini qəbul edərək məhsulları filter-ləyəcək. Filterlənən məhsullar GOODS variable-ına yerləşdirilərək, şablona göndəriləcək.
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page)) 

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