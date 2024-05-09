from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    # 1) Data-lari verilenler bazasindan aliriq. Ancaq muveqqeti olaraq bir data gonderek ki, yoxlayaq nece bu data-lari sablonda eks etdirmek olar.
    context = {
        'title' : 'Home',
        'content' : 'Home page of magazines - HOME',
        # 3) Ferli tiplerde deyerler gondermeyi yoxlayaq.
        'list' : ['first', 'second'],
        'dict' : {'first': 1},
        'bool' : True
    }

    # 2) CONTEXT adli variable-i, render() funksiyasina 3cu parametr olaraq veririk. Sonra index.html faylinda {{ }} simvollarindan istifade ederek
    # bu CONTEXT icinde olan acar sozleri yazaraq deyerlerini elde edirik. CONTEXT sozunu yazmaq lazim deyil. Bir basa acar sozleri yazmaq kifayetdir.
    return render(request, 'main/index.html', context)




def about(request):
    return HttpResponse('About page')