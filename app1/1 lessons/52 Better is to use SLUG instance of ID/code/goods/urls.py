from django.urls import path
from goods import views
app_name = 'goods'

urlpatterns = [
    path('',         views.catalog, name='index'),

    # 1) INT tipini SLUG tipi ile evez edirik ve parametr adinida 'product_slug' olaraq deyisdiririk. 
    path('product/<slug:product_slug>/', views.product, name='product'),
]