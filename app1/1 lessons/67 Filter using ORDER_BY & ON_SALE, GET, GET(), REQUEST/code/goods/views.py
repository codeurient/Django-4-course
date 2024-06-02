from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Products


def catalog(request, category_slug):
    page     = request.GET.get('page', 1)
    # 1) REQUEST-den deyerleri elde etmek ucun GET() metodundan istifade edirik. Elde edilen deyerleri VARIABLE-llara yerlesdiririk. Sonra IF ile sorgu yaradaraq uyğun PRODUCT-u göstər deyirik. 
    on_sale  = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug = category_slug))

    # 2) __GT (greater than) demekdir. Yəni DB-de ki DISCOUNT sahesi 0-dan boyuk olanlari filtirləsin demişik. Bu sadəcə endirimdə olan məhsulları əldə etməyimizə köməklik göstərəcək. 
    if on_sale:
        goods = goods.filter(discount__gt=0)
    # 3) ORDER_BY() metodunun içində PRİCE sütunun adını yazaraq qiymətə görə sırala deyirik. Əgər PRİCE stringinin önünə - (mənfi) qoysaq onda azalan sıra ilə sıralamış olacağıq. 
    # DEFAULT deyilən bir sütun olmadığı üçün ORDER_BY != 'DEFAULT' yazdıq ki, əgər həmin İNPUT seçilərsə onda İF işləməyəcək. 
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