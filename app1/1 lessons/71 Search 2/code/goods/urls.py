from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    # 1) SEARCH marşrutunu digər marşrutlardan yuxarıda yazmaq lazımdır. Əks halda SEARCH marşrutuna sorğu gəlib çatmayacaq və məhsulu tapa bilməyəcəyik. Name atributunun da adini SEARCH edirik. 
    path('search/',                       views.catalog, name='search'),
    path('<slug:category_slug>/',         views.catalog, name='index'),
    path('product/<slug:product_slug>/',  views.product, name='product'),
]