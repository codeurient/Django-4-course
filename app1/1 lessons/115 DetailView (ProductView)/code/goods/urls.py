from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('search/',                       views.catalog, name='search'),
    path('<slug:category_slug>/',         views.catalog, name='index'),
    # 1) 
    path('product/<slug:product_slug>/',  views.ProductView.as_view(), name='product'),
]