from django.contrib import admin

from users.models import User

# 1) Sadə formada qeydiyyata alırıq. Sonra    VERBOSE_NAME    əlavə etmək üçün daxil oluruq     USERS/APPS.PY     faylına.   VERBOSE_NAME ilə ADMİN paneldə DEFAULT olaraq USER adlanan
# sahənin adını dəyişdirə bilirik. 
admin.site.register(User)


