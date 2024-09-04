from django.http import Http404
from django.views.generic import DetailView, ListView
from goods.models import Products
from goods.utils import q_search




# 2) Proqramı bu cür işə saldıqda artıq işlədiyini görəcəyik. Bütün məhsullar əks olunacaq. 

class CatalogView(ListView):
    # 3) model    variable-ına   Products   dedikdə bu köhnə qayda ilə yazılan    `Products.objects.all()`     bu yazıya bərabərdir.   Yəni bütün məhsulları əldə edirik bu qayda ilə. 
    model = Products   
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    # 1) Pagination yaratmaq ucun   `paginate_by`     adlı variable yaradırıq.  Ancaq hələki işləməyəcək. 
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Catalog"
        # 5) Proqramı işə saldıqdan sonra      `{% url "catalog:index" slug_url %}`       bu cür xəta verməməsi üçün müvəqqəti    `slug_url`      göndəririk şablona.
        context["slug_url"] = "asdasdasdas"
        return context
    # 4) VIEWS.PY     faylında da dəyişiklik etdikdən sonra proqramı işə salaraq baxa bilərik. 


















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