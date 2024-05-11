from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    context = {
        'title' : 'Home - main',
        'content' : 'Furniture store HOME',
    }
    return render(request, 'main/index.html', context)



def about(request):
    context = {
        'title' : 'Home - about',
        'content' : 'Here is some text about us',
        'text_on_page': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ',
    }
    return render(request, 'main/about.html', context)


