from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/',         views.catalog, name='index'),
    # 1) Marşrutu sildik çünki, dəyərləri GET sorğunun REQUEST parametri ilə verəcəyik. Marşrut olaraq isə yuxarıdaki ƏSAS marşrutu istifadə edəcəyik. 
    path('product/<slug:product_slug>/', views.product, name='product'),
]