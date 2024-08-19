from django.contrib import admin


from orders.models import Order, OrderItem

# 1) ADMIN PANEL-in daha səliqəli görsənməsi üçün aşağıdakı kimi yazırıq.

# admin.site.register(Order)
# admin.site.register(OrderItem)


# 7) Buda  OrderAdmin()   class-ına bağlı olan    OrderItemTabulareAdmin()  class-ıdır.  Bu class ORDER-ə daxil olduqda aşağıda həmin ORDER-ə aid olan məhsulları göstərmək üçündür.
class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity"
    search_fields = (
        "product",
        "name",
    )
    # 8) EXTRA variable-ına 0 (sıfır) verdikdə manual məhsul əlavə etmək üçün olan  ekstra görünən sahələri gizləmiş oluruq. 
    extra = 0




# 9) Eyni işləri    Orderİtem    model-i üçündə edirik. 
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "quantity"
    search_fields = (
        "order",
        "product",
        "name",
    )


# 10) Order model-ini yaradırıq ancaq bu model-i istifadə edəcəyik USER model-i üçün. Yəni ADMİN PANEL-də USER-lara daxil olduqda həmin USER-in hansı ORDER-ləri olduğunu görmək üçün
# 11) Sonra daxil oluruq USER model-inə və İNLİNES variable-ından istifadə edərək bu    OrderTabulareAdmin()    class-ını   USER ilə əlaqələndiririk. 
class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "requires_delivery",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0






# 2) İlk öncə ORDER model-ini Qeydiyyata alırıq. 
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # 3) ADMİN PANEL-də görmək istədiyimiz sütun adlarını LİST_DİSPLAY ilə bildiririk.
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    # 4) Axtarış üçün istifadə edilən sütun adını qeyd edirik. Birdən çox sütun adı qeyd etmək olar. Biz İD üzrə axtarış edəcəyik. 
    search_fields = (
        "id",
    )
    # 5) Bu sütun sadəcə oxunmaq üçündür deyirik. Yəni redaktə edilə bilməz. 
    readonly_fields = ("created_timestamp",) 
    # 6) Sağ tərəfdə FİLTER menusu açılacaq və hansı sahələr üzrə axtarış edə bilərik deyə qeyd etmişik. 
    list_filter = (
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
    )
    # 6) İNLİNES isə, İD-ni klikləyərək ORDER-ə daxil olduqda aşağıda ORDERİTEM modelindəki, bu ORDER-ə bağlı olan sifariş edilmiş məhsulları görmək üçündür. 
    inlines = (OrderItemTabulareAdmin,)
