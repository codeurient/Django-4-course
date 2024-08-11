from django.contrib import admin

from users.models import User

# 1) Admin panelde USER ilə bağlı dəyişiklər etmək üçün aşağıdakı kodu kommentə alaraq @ADMİN dekaratrou və REGİSTER() metodu ilə qeydiyata salırıq.
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', ]
    search_fields = ['username', 'first_name', 'last_name', 'email', ]