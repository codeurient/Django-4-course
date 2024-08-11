from django.contrib import admin

from users.models import User
from carts.admin import CartTabAdmin



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', ]
    search_fields = ['username', 'first_name', 'last_name', 'email', ]

    # 1) CartTabAmin()     klasını yaratdıqdan sonra bu klası       USERS / ADMİN.PY      faylında İNLİNES adlı variable-a verərək CARTS ilə USERS-ı bir birlərinə bağlaya bilərik.
    inlines = [CartTabAdmin, ]


    