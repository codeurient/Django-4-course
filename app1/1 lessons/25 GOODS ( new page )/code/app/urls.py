from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    # 1) App qovlugundaki URLS.PY faylinda, GOODS ilə əlaqəli olan marşrutları qeydiyyata alırıq. 
    path('catalog/', include('goods.urls', namespace='catalog'))
]

# 2) Hal-hazırki bütün marşrutlar bu cür görsənir:

# www.example.com/admin/
# www.example.com/
# www.example.com/about/
# www.example.com/catalog/
# www.example.com/catalog/product