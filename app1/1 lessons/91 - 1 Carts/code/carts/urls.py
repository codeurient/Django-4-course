from django.urls import path

# 1) Səbət ilə işləməyə başalamazdan əvvəl ilk olaraq səbətin saytda haralarda istifadə edildiyinə göz gəzdirmək lazımdır.

# a) Profile səhifəsində
# b) Bütün səhifələrdə sol tərəfdə yerləşən balaca səbət ikonu
# c) HEADER hissədə yerləşən səbət linki

# Deməli səbət ilə əlaqə olan səhifəni yaradaraq onu, digər bütün yerlərə İNCLUDE tag-i vasitəsi ilə çağırmaq olar. 


from carts import views

app_name = 'carts'

# 2) İndi isə Səbət üçün 3 dənə link yaradırıq.
urlpatterns = [
    # a) ADD linki ilə səbətə məhsul əlavə edəcəyik
    path('cart_add/<int:product_id>',        views.cart_add,         name='cart_add'),
    # b) CHANGE linki ilə səbətə əlavə edilən məhsulu dəyişdirə biləcəyik
    path('cart_change/<int:product_id>',     views.cart_change,      name='cart_change'),
    # a) REMOVE linki ilə səbətə əlavə edilən məhsul silə biləcəyik
    path('cart_remove/<int:product_id>',     views.cart_remove,      name='cart_remove'),
]

# 3) Sonra daxil oluruq     APP/SETTINGS.PY    faylına ki, yuxarıdakı linkləri İNCLUDE edək.




