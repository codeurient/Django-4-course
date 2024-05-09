from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # 1) namespace haqqinda MAIN icindeki URLS faylinda yazi var.
    path('', include('main.urls', namespace='main'))
]