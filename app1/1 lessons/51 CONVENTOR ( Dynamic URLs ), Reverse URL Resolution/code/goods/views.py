from django.shortcuts import render

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        "title": "Home - Catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)  


# 1) GOODS/URLS.PY faylindan gonderilen CONVENTOR-u      path('product/<int:PRODUCT_İD>)       bu fayl içində əldə edirik.  Əldə etdiyimiz DƏYƏR məhsulun İD-si olacaq.
def product(request, product_id):
    # 2) Artiq DB-sə müraciət edərək, GET() metodu ilə müəyyən İD-yə uyğun gələn məhsulu götürə bilərik. Məsələn: get(id=7)    __________    ID-si 7 olan mehsul.
    #! DJANGO-da istifadə edilən GET() metodu ilə PYTHON-da istifadə edilən GET() metodu fərqlidir.
    product = Products.objects.get(id=product_id)

    # 3) Sonra CONTEXT yaradiriq ve elde edilen mehsulu Şablona göndəririrk.
    context = {
        'product': product
    }

    return render(request, "goods/product.html", context=context)    