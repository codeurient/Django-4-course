from django.shortcuts import render

# 2) DB-den melumatlarimizi cagirmaq ucun model-i IMPORT 
from goods.models import Products


def catalog(request):

    # 2) Bu melumatlari 'goods' adli variable icine qoyuruq   
    goods = Products.objects.all()

    context = {
        "title": "Home - Catalog",
        # 3) Manul olan data-lari silerek yuxarida yaratdigimiz 'goods' variable-ini DICT icindeki 'goods' xassesine yerlesdiririk. Bu melumatlari artiq 
        # evvelki derslerde şablonda çağıraraq yerləşdirmişik: GOODS/TEMPLATES/GOODS/CATALOG.HTML
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)  


def product(request):
    return render(request, "goods/product.html")