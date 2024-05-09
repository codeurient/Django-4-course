from django.urls import path

# 1) 
from goods import views
app_name = 'goods'

urlpatterns = [
    # 2) Birinci URL bizi mehsullarin kataloquna yonlendirecek 
    path('', views.catalog, name='index'),

    # 3) Ikinci URL bizi deqiq bir mehsula yonlendirecek
    path('product/', views.product, name='product'),
]