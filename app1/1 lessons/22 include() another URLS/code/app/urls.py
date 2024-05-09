from django.contrib import admin
from django.urls import include, path


# 1) Tetbiq boyudukce butun URL adresleri bir fayl icin (urls.py) tutmaq cetinlesecek. Hansi URL adresin hansi sehifeye aid oldugunu tapmaq 
# çətin olacaq. Buna görə də, hər tətbiq yəni hər səhifə üçün URLS.PY adında fayl yaradırıq və hər tətbiqin öz URL-sini həmin faylda yazırıq. 
# Hər URLS.PY faylınıda hər tətbiq üçün yaratmış olduğumuz qovluqda yaratmaq lazımdır.
urlpatterns = [
    path('admin/', admin.site.urls),

    # 2) BASE sehifesi ucun olan URL adresleri APP qovlugunda olan URLS.PY faylindan goturduk ve MAIN qovlugunda yaratdigimiz URLS.PY faylina qoyduq.
    # İndi ise MAİN qovlugunda olan URLS.PY faylının özünü APP qovluğunda olan URLS.PY faylına İNCLUDE() etmek lazımdır. Bunun üçün İNCLUDE() metodu 
    # içində string formatında aşağıdakı kimi yazırıq. Ancaq MAİN sehifesi bizim esas ANA sehifemiz oldugu ucun PATH() metodunun 1ci parametrini boş
    # string kimi yazmalıyıq. 
    path('', include('main.urls'))
    # 3) Əgər bu cür yazsaydıq: path('main', include('main.urls'))  Onda brauzerdə ana sehifeyə daxil olmaq ucun bele yazmaliydiq: http://127.0.0.1:8000/main
    # Və əgər http://127.0.0.1:8000 bu cür yazsaydıq onda xəta alacaqdıq ki, belə bir səhifə mövcud deyil.

]