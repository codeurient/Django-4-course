from django.urls import path

from main import views

urlpatterns = [

    # 1) Syatimiz isleyir ancaq tam dogru yox. Cunki name='index' istifade edilmis ola biler hemin MAIN sehifesi ucun hem CART sehfesi ucun. Onda 
    # proqram hardan bilecek ki, hansi INDEX hansi sehifeye aiddir. Bunun ucun APP/URLS.PY qovlugunda INCLUDE() metoduna 2ci parametr olaraq
    # 'namespace' yaziriq. Bu parametrə ad verdikdə şablonda da qeyd etmək lazımdır ki, mövcud İNDEX namespace-i MAİN olan URL adresə aiddir:

    #!  <li><a class="dropdown-item  text-white" href="{% url "main:about" %}">   About us   </a></li>

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]