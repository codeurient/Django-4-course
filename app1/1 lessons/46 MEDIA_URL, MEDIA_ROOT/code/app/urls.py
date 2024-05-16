from django.contrib import admin
from django.urls import include, path

# 2) Və dokumentasiyada yazibdir ki, STATIC metodunu istifade ede bilmek ucun IMPORT etmek lazimdir. 
from django.conf.urls.static import static

# 3) DEBUG constanti SETTINGS icinde yerlesirdi onun ucun bu cur yazmisdiq:                                             from app.settings import DEBUG.
# İndi aşağıda MEDIA_URL və MEDIA_ROOT constantlarinida istifade edirik deye onlarida IMPORT-a elave etmeliyik:         from app.settings import DEBUG, STATIC_URL, STATIC_ROOT
# Yaxud daha qisa olmasi ucun bu cur de yaza bilerik. Onda Constantlarin onune SETTINGS elave etmeliyik:                from app import settings
from app import settings
#! NOT: Eger birden bu SETTINGS islemese onda asagidaki linke-e gederek dakumentsaiyada olan bu SETTINGS-i import etmek lazimdir:     from django.conf import settings
#! Cunki hal-hazirki SETTINGS bizim APP qovlugunda olan SETTINGS.PY faylidir. Ancaq yuxaridaki SETTINGS diger yəni ən əsas yəni  
#! daha dərində yerləşən kök fayldır. 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',         include('main.urls',  namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog'))
]

if settings.DEBUG:
    urlpatterns += [  
            path("__debug__/", include("debug_toolbar.urls"))  
        ]
    



    # 1) SETTİNGS.PY faylında yolu təyin edərək MEDIA_ROOT constantına qoyduqdan sonra URLS.PY faylında həmin yolu STATİC() metodu ilə qeydiyyata almalıyıq. 
    # static() metodu yerləşməlidir URLPATTERNS variable içində. Bu haqqda dokumentasiyada yazıbdır: https://docs.djangoproject.com/en/5.0/howto/static-files/
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









# 4) Indi proyekti işə salırıq və admin panelə gedərək şəkilləri yükləyirik. 