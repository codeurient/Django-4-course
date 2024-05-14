from django.contrib import admin
from django.urls import include, path

from app.settings import DEBUG


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',         include('main.urls',  namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog'))
]

#! 1) Bu YOL ancaq DEBUG rejimdə əlavə edilsin deyirik. DEBUG rejim bizə ancaq proqramı yığanda lazım olduğu üçün belə edirik. DEPLOY etdikdə lazım deyil. 
if DEBUG:
    urlpatterns += [  path("__debug__/", include("debug_toolbar.urls"))  ]