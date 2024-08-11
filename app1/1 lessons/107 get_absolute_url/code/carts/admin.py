from django.contrib import admin
from carts.models import Cart

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "product", "quantity", "created_timestamp"            
    search_fields = "product", "quantity", "created_timestamp"      
    readonly_fields = ("created_timestamp", )                      
    extra = 1                                                                                      


# Admin Panelde anonim olan istifadeci adini ve mehsulun adini eks etdirmek ucun asagidaki addimlari izleyek. 

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # 3) Sonra isə aşağıdakı metod adlarını LİST_DİSPLAY içində STRİNG kimi çağırırıq. 
    list_display = ['user_display', 'product_display', 'quantity', 'created_timestamp',]
    list_filter =['created_timestamp', 'user', 'product__name',]

    # 1) USER_DISPLAY() adında metod yaradırıq. OBJ isə DJANGO-nun daxili parametridir. CART modelinde ForeignKey sayəsində USER modelimiz mövcud olduğu üçün bilavasitə bu parametr ile .USER yazaraq mövcud istifadəçini əldə edirik.
    def user_display(self, obj):
        if obj.user: # Əgər belə bir istifadəçi varsa onu return edirik əks halda  'Anonymous user' stringini əldə ediri. 
            return str(obj.user)
        return 'Anonymous user'
    
    # 2) Bir metod da PRODUCT NAME üçün yazırıq. Bu model üçün də ForeignKey mövcud olduğu üçün bilavasitə OBJ parametri ilə .PRODUCT yazaraq məhsul adını əldə edirik. 
    def product_display(self, obj):
        return str(obj.product.name)
    


    