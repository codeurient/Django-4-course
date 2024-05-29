from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/',         views.catalog, name='index'),
    # 1) GOODS/VIEWS.PY faylındaki PAGE parametrinə fərqli ədədlər göndərmək üçün yeni bir marşrut yaradırıq və INT adlı conventoru həmin marşruta əlavə edirik. 
    #    Bu marşrutda yazmış olduğumuz PAGE parametri bizim URL yerində yazdığımız ƏDƏD-ləri əldə edir və GOODS/VIEWS.PY controllerində ki, PAGE parametrinə ötürür:        http://127.0.0.1:8000/catalog/all/2
    path('<slug:category_slug>/<int:page>/',         views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]

# 2) Bu PAGE parametri ŞABLON-da olan 1,2,3,4 ve.s paginator-u klikləndikdə həmin rəqəmləri avtomatik qəbul etməlidir. Bunun üçün gedirik, GOODS/TEMPLATES/GOODS/CATALOG.PY   faylına......   59-cu dərs.....