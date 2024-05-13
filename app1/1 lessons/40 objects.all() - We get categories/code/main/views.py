from django.http import HttpResponse
from django.shortcuts import render

# 1) Web sehifede produktlarin kateqoriyalarini gostermek ucun CATEGORIES modelini (cədvəlini) IMPORT edirik. 
from goods.models import Categories

def index(request) -> HttpResponse:
    # 2) CATEGORİES klasinin OBJECTS menecerinin all() metodu vasitesi ile elde etdiyimiz mehsullarin kateqoriyalarini, aşağıda 'categories' adında yaratdığımız variable-a yerləşdiririk.
    # all() metodu ile DB-dən əldə etdiyimiz bütün məlumatlar QUERYSET olaraq CATEGORİES variable-ina yerləşdiriləcək. #! Şəkil iki.
    categories = Categories.objects.all()


    context = {
        'title' : 'Home - main',
        'content' : 'Furniture store HOME',
        # 3) 'categories' variable-ini şablona göndərmək üçün həmin variable-ı qoyuruq 'CONTEXT' dict-inin içinə. Sonra 'MAIN/TEMPLATES/MAIN/BASE.HTML' faylına gedərək bütün kateqoriya adlarını 
        #     {% for category in categories %}   for konstruktoru ilə ekrana yazdırırıq.
        'categories' : categories,
    }
    return render(request, 'main/index.html', context)



def about(request):
    context = {
        'title' : 'Home - about',
        'content' : 'Here is some text about us',
        'text_on_page': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ',
    }
    return render(request, 'main/about.html', context)