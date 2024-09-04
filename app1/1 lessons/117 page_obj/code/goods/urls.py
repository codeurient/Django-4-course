from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    # 2) 
    path('search/',                       views.CatalogView.as_view(), name='search'),
    # 1) 
    path('<slug:category_slug>/',         views.CatalogView.as_view(), name='index'),
    path('product/<slug:product_slug>/',  views.ProductView.as_view(), name='product'),
]