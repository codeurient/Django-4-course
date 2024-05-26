from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    # 1)  Seçilən kateqoriyaya uyğun gələn mehsulu gostermek ucun yenə conventor-dan istifadə edəcəyik..    'category_slug' parametri <A> taginin onundeki yazini elde edir ve bizde bu parametri CONTROLLER-ə gonderirik.
    path('<slug:category_slug>/',         views.catalog, name='index'),


    path('product/<slug:product_slug>/', views.product, name='product'),
]