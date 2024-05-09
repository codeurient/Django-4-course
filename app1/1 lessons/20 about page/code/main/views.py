from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    context = {
        'title' : 'Home - main',
        'content' : 'Furniture store HOME',
    }
    return render(request, 'main/index.html', context)



# 1) About sehifesi ucun ferqli metnler elave ederek render etdik. 
def about(request):
    context = {
        'title' : 'Home - about',
        'content' : 'Here is some text about us',
        # 2) Iki yaxud daha çox söz olduqda onda birlesmeni altdan xett ile yazmaq meslehetdir yoxsa şablon basa dusmur.
        'text_on_page': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ',
    }
    return render(request, 'main/about.html', context)


