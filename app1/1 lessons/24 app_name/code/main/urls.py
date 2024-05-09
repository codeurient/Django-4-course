from django.urls import path

from main import views

# 1) Serveri sondurub yeniden acdiqda APP/URLS.PY faylinda, şəkildə gosterildiyi kimi bir xeta aliriq. Bu xeta da deyilir ki, NAMESPACE istifade etdikde
# hemin NAMESPACE adini APP_NAME deyiskenine elave etmek lazimdir. Asagida bunu edirik ve xeta aradan qalxir.
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]