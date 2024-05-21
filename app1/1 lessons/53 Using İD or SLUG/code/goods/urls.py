from django.urls import path
from goods import views

app_name = 'goods'


urlpatterns = [
    path('',         views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),

    # 1) Bir kontroller birden cox URL marşrut qəbul edə bilər. Məsələn: bu fayl icinde 2ci URL-i gonderirik ve gedib Controller-de qebul edirik. 
    path('product/<int:product_id>/', views.product, name='product'),
]






#! NOT: Birinci ID yazilmalidir,   Ikinci SLUG yazilmalidir.    Eks halda xeta alariq.   Cunki URL yerinde Reqem yazdiqda 1ci axtaris SLUG uzre oldugundan proqram hemin REQEMI 
#! STRING formatina cevirir.   Onun ucun ILK siraya INT conventor-unu qoyuruq.  

# Yuxarida yazdigimizi bununla evez edeceyik:

# urlpatterns = [
#     path('',         views.catalog, name='index'),
#     path('product/<int:product_id>/', views.product, name='product'),
#     path('product/<slug:product_slug>/', views.product, name='product'),
# ]