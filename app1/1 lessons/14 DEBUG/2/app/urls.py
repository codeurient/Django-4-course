from django.contrib import admin
from django.urls import path
from main import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # 1) Birinci parametrde marsrut adı olaraq istenileni yazmaq olar. Ikinci parametrde ise ABOUT, funksiyamiza link vermisik. Yəni funksiyani cagirmisiq.
    # ucuncu parametr ise hemin url-i view icinde hansi adla cagiracagimizi teyin edir. PATH funksiyasinin ustune kursoru getirdikde ->URLPattern bele bir
    # yazi goreceyik. Bu onu bildirir ki, hemin funksiya, URL ile bagli informasiyani return edir.
    path('about/', views.about, name='about'),

    # Istifadeci URL yerinde bir seyler yazdiqda, brauzer avtomatik olaraq hemin istifadeci haqqinda olan butun melumatlari servere gonderir. PATH metodu da
    # bu melumatlari serverden alaraq REQUEST parametrine yerlesdirir.
]