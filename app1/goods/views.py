from django.shortcuts import render

# 1) Goods sehifesi ucun Controller yaradiriq. 
def catalog(request):
    return render(request, 'goods/catalog.html')

def product(request):
    return render(request, 'goods/product.html')