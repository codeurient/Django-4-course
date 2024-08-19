from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from app import settings


urlpatterns = [
    path('admin/'   ,   admin.site.urls),
    path(''         ,   include('main.urls'   ,   namespace='main')),
    path('catalog/' ,   include('goods.urls'  ,   namespace='catalog')),
    path('user/'    ,   include('users.urls'  ,   namespace='user')),
    # 1) CARTS ucun marşrut təyin edirik. Sonra gedirik    VIEWS.PY    controller-inə. 
    path('cart/'    ,   include('carts.urls'  ,   namespace='cart')),
]

if settings.DEBUG:
    urlpatterns += [  
            path("__debug__/", include("debug_toolbar.urls")),  
        ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    