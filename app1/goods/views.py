from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView
from goods.models import Products
from goods.utils import q_search

def catalog(request, category_slug = None):
    page     = request.GET.get('page'    , 1)
    on_sale  = request.GET.get('on_sale' , None)
    order_by = request.GET.get('order_by', None)
    query    = request.GET.get('q'       , None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug = category_slug)
        if not goods.exists():
            raise Http404()

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


















# 1) Ilk öncə    `ProductView`    adında class yaradırıq və   `DetailView`    adlı class-ı izləməsini deyirik. 
class ProductView(DetailView):
    # 2) Sonra  `Product` adlı modelimizi    `MODEL`  adlı variable-a yerləşdirə bilərik ancaq bu yanaşma doğru olmaz çünki belə yazdıqda bütün məhullar əldə edilir. Bizə isə 1 məhsul lazımdır.
    #! model = Products
    template_name = "goods/product.html"


    # 4) get_object()    metodunda məhsulu SLUG adına görə əldə etməyimiz üçün, Djangonun daxili       `SLUG_URL_KWARG`       adlı variable-ından istifadə edirik. Bu variable,  GOODS / VIEWS.PY 
    #    faylında yerləşən URL içindən    `product_slug`      conventor-unu avtomatik əldə edir. 
    slug_url_kwarg = 'product_slug'


    # 6) get_object() metodu nəticəni RETURN etdikdə, DJANGO default olaraq OBJECT adında CONTEXT yaradır və bu adı şablonda istifadə edərək RETURN olan dataları şablonda əks etdirə bilərik.
    #    Ancaq biz şablonda   `PRODUCT`  adı ilə dataları əks etdiririk. Buna görədə OBJECT adını PRODUCT adı ilə əvəz etmək üçün aşağıdakı kimi       `context_object_name`      yazmaq lazımdır. 
    context_object_name = 'product'




    # 3) Bir məhsul əldə etmək üçün    `get_object()`   adlı daxili metotdan istifadə edə bilərik. 
    def get_object(self, queryset = None):
        # 5) Sonra GET()  meotdu ilə   DB   olan cədvəlimizin SLUG sütununa müraciət edərək bir məhsulu həmin      `product_slug`-a     əsasən əldə edirik. 
        product = Products.objects.get(slug = self.kwargs.get(self.slug_url_kwarg))
        return product
    



    # 7) Əlavə olaraq CONTEXT göndərmək üçün şablona GET_CONTEXT_DATA  metodundan istifadə edirik.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 8) Aşağıda    OBJECT    yazısı bizim yuxarıdakı      GET_OBJECT  metodunun RETURN etdiyi PRODUCT-dur. Yuxarıda da qeyd etdikki Django default olaraq OBJECT adı ilə return edir. Onun üçündə
        #    bizdə bu cür OBJECT yazaraq PRODUCT modelinə müraciət edirik və NAME sahəsinin dəyərini şablona göndəririk. 
        context["title"] = self.object.name
        return context