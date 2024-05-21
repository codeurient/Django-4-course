from django.shortcuts import render
from goods.models import Products


def catalog(request):
    goods = Products.objects.all()
    context = {
        "title": "Home - Catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)  



# 1) PRODUCT_ID -ni de parametr olaraq diger parametr yanina elave edirik. Bele olduqda her 2 parametride istifade etmek ucun IF -den faydalanmaq lazimdir.
# IF istifade etdikde, PRODUCT_ID ve PRODUCT_SLUG parametrlerine default olaraq FALSE deyerini vermeliyik. Şablonda hər hansısa bir məhsulu seçdikdə bu FALSE dəyəri həmin məhsulun 
# İD-si yaxud SLUG-ı ilə əvəz ediləcəkdir. 
def product(request, product_slug = False, product_id = False):
    # 2) eger sorgu ID uzre aparilarsa, yəni URL yerində   ->   http://127.0.0.1:8000/catalog/product/1      bele yazilarsa  onda mehsulu  ID-yə görə əldə edək
    if product_id:
        product = Products.objects.get(id=product_id)
    # 3) Əks halda sorgu SLUG uzre aparilsin və mehsulu SLUG-a görə əldə edək
    else:
         product = Products.objects.get(slug=product_slug)


    context = {
        'product': product
    }
    return render(request, "goods/product.html", context=context)    