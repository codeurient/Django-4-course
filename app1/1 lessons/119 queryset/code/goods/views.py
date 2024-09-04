from django.http import Http404
from django.views.generic import DetailView, ListView
from goods.models import Products
from goods.utils import q_search


class CatalogView(ListView):
    # 1) Indi isэ MODEL-imizi açırıq. Çünki aşağıda İF içində məhsulları əldə etmək üçün bu modeldən istifadə etmək daha doğru olacaqdır. 
    model = Products   

    # 6) Əgər məhsulları xüsusi ORM metodları ilə filterləyərək əldə etmək istəsəydik onda yuxarıda olan model-i yenidən kommentə alaraq, əvəzində QUERYSET adlı variable yaradaraq ona bu dəyəri verə bilərdik:   Products.objects.all()
    #    Sonra isə ORM metodlarını yazaraq həmin məhsulları DB-dən artıq filterlənmiş formada əldə edə bilərik:         queryset = Products.objects.all().order_by('-id')  
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    paginate_by = 3
    # 5) Əgər məhsul yoxdursa 404 səhifəsini görək. 
    allow_empty = False
    # 8) slug_url_kwarg
    slug_url_kwarg = "category_slug"

    def get_queryset(self):
        # 9) slug_url_kwarg
        category_slug = self.kwargs.get(self.slug_url_kwarg)
        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")

        if category_slug == 'all':
            # 2) Burada isə GET_QUERYSET() metodu ilə modeldən bütün (all) məhsulları əldə edirik. 
            goods = super().get_queryset()
        elif query:
            goods = q_search(query)
        else:
            # 3) Və burada eyni qayda ilə bütün məhsulları əldə edərək filterləyirik onları. 
            goods = super().get_queryset().filter(category__slug = category_slug)
            # 4) Əgər məhsul yoxdursa 404 error səhifəsi ekranda görmək üçün aşağıdakı kodları yazmışıq ancaq bunu   `allow_empty`    variable-ına FALSE dəyərini verərərkdə etmək olardı. (yuxarıda yazmışıq)
            if not goods.exists():
                raise Http404()

        if on_sale:
            goods = goods.filter(discount__gt=0)
        if order_by and order_by != "default":
            goods = goods.order_by(order_by)
        return goods

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Catalog" 
        # 7) Aşağıda GET() metoduna  verilən            'category_slug'         stringini hər hansısa bir   variable içinə qoyduqdan sonra da dinamik olaraq yazmaq olar. Məsələn:   slug_url_kwarg = "category_slug"
        context["slug_url"] = self.kwargs.get(self.slug_url_kwarg)
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