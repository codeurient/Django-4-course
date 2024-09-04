from django.http import Http404
from django.views.generic import DetailView, ListView
from goods.models import Products
from goods.utils import q_search





class CatalogView(ListView):
    model = Products   
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    # 1) Pagination-ının işləməmə səbəbi şablonda onun fərqli context variable olaraq istifadə edilməsidir. Yəni məsələn bütün məhsulları əldə etmək üçün GOODS adında context variable var və biz bunu
    # yuxarıda    `context_object_name`     içində qeyd etdik.    Ancaq paginator üçün      `page_obj`     adında context variable istifadə edilməlidir şablonda (goods / templates / goods / catalog.html ) və biz bunu qeyd etməmişik. 
    paginate_by = 3
    # 2) Şəkil nömrə ikidə işarələnən yerlər dəyişdirilərək əvəzində   `page_obj`    yazmaq lazımdır. 



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Catalog"
        context["slug_url"] = "asdasdasdas"
        return context














class ProductView(DetailView):
    template_name = "goods/product.html"
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'


    def get_object(self, queryset = None):
        product = Products.objects.get(slug = self.kwargs.get(self.slug_url_kwarg))
        return product
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context