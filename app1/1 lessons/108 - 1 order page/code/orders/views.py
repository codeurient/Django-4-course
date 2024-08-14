from django.shortcuts import render


# 1) Controller üçün metodumuzu yaradırıq. 
def create_order(request):
    return render(request, 'orders/create_order.html')