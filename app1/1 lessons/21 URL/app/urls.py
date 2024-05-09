from django.contrib import admin
from django.urls import path
from main import views



# 1) BASE.HTML faylinin icinde ferqli sehifelere kecmek ucun naviqasiya ( <a> tag-leri) paneli vardir. 
# a) Home sozunu basanda home sehifesine gede bilmeliyik
# a) About sozunu basanda home sehifesine gede bilmeliyik
# a) Cart sozunu basanda home sehifesine gede bilmeliyik ve.s
# Bu <a> tag-lerinin icinde marsrut olaraq URL yazmaq lazimdir.( admin/  yaxud  about/  ve.s kimi).
# Ancaq URL yol yazmaq evezine ( name='index' ) bu cür psevdonim yazada bilerik:  <a class="navbar-brand" href="{% url "index" %}"> Home </a>
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]