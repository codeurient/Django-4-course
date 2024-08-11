from django.contrib import admin
from carts.models import Cart

# 4) Normalda ADMİN paneldə USERS bölməsinə keçdikdə istifadəçi adlarını görə bilərik və istifadəçilərdən birini seçdikdə həmin səhifədə bu istifadəçi haqqında məlumatlar əks olunur yalnız bu istifadəçinin hansı məhsullara sahib olduğu
#    görünmür.  Ancaq elə edə bilərik ki, hər istifadəçinin səbətə əlavə etdiyi bütün məhsulları aşağıda əks edilsin:       http://127.0.0.1:8000/admin/users/user
class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "product", "quantity", "created_timestamp"             # Məhsul haqqında görəcəyimiz sütunlar
    search_fields = "product", "quantity", "created_timestamp"      # Hansı sahələr üzrə axtarış edə bilərik
    readonly_fields = ("created_timestamp", )                       # Bu sahə redaktə edilə bilməz 
    extra = 1                                                                                       # Manual olaraq özümüz hansı məhsulu əlavə edə bilərik istifadəçi üçün

    # 5) CartTabAmin()     klasını yaratdıqdan sonra bu klası       USERS / ADMİN.PY      faylında İNLİNES adlı variable-a verərək CARTS ilə USERS-ı bir birlərinə bağlaya bilərik. 107 nömrəli dərsdə....





# 1) Burada da Admin panel ucun bezi deyisiklikler edirik. 
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # 3) Ancaq LIST_DISPLAY üçün ForeignKey əlaqəsi dəstəklənmədiyindən burada PRODUCT__NAME yaza bilmərik:   list_display = ['user', 'product', 'quantity', 'created_timestamp',]
    list_display = ['user', 'product', 'quantity', 'created_timestamp',]
    # 2) Baxmayaraq ki, biz CART modelinin icindeyik ve bu modelin icinde 'PRODUCT' adında FOREİGN KEY sütunu var buna görədə bilavasitə həmin 'PRODUCT' sütunu vasitəsi ilə, __STR__ metodu avtomatik FİLTER bölməsində bu adları əks etdirəcək. 
    #    Həmin adları dəyişdirə bilərik. Bunun üçün PRODUCT__NAME yazırıq. Yəni, PRODUCT modelinin NAME sütununu çağırırıq:   list_filter =['created_timestamp', 'user', 'product',]
    list_filter =['created_timestamp', 'user', 'product__name',]



