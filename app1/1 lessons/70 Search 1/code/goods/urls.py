from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/',         views.catalog, name='index'),
    # 1) SEARCH sahesi üçün yeni marşrut yaradırıq. 
    path('search/',                       views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]