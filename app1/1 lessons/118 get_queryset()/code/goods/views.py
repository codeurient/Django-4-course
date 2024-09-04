from django.http import Http404
from django.views.generic import DetailView, ListView
from goods.models import Products
from goods.utils import q_search




# 1) Məhsullar səhifəsində filter sistemimizdə mövcuddur. Köhnə qayda ilə    'on_sale',     'order_by'    və.s əldə edərək istifadə edirdik və eynisini yeni qayda ilədə etmək lazımdır. 
class CatalogView(ListView):
    # 2) İlk öncə    model    variable-ını silirik yaxud kommentə alaq. Artıq o lazımd deyil. Çünki bu qayda ilə bütün məhsulları əldə edirdik. Aşağıda isə   GET_QUERYSET() metodundan istifadə edərək
    #    yenə eyni PRODUCT-u əldə edəcəyik ancaq daha geniş funksionallıqları olacaq hansı ki, bu funksionallıqlar bizə imkan verəcək ki, 'on_sale',     'order_by'   və.s kimi sorğuları əldə edək. 
    #! model = Products   
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    paginate_by = 3

    # 3) 
    def get_queryset(self):
        # 4) Ilk öncə    URLS.PY   faylındakı   CATEGORY_SLUG  conventor-unu əldə edirik. 
        category_slug = self.kwargs.get("category_slug")
        # 5) Sonra FORM-dan GET sorğu ilə gələn filtir parametrlərini əldə edirik. 
        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")

        # 6) Bu hissə köhnə kodda olan hissə ilə eynidir.
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

        # 7) Sonra isə nəticəni return edirik.
        return goods
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Catalog"
        context["slug_url"] = self.kwargs.get('category_slug')
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