from django.contrib import admin

# 1) Proqramı işə salaraq onun işləyib i.ləmədiyini yoxlamaq üçün, həmin modelləri qeydiyyata salmaq lazımdır. 

from orders.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)



