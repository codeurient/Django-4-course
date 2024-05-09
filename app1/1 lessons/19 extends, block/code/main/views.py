from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    
    #! 1)
    context = {
        'title' : 'Home - main',
        'content' : 'Furniture store HOME',
    }

    return render(request, 'main/index.html', context)



def about(request):
    return HttpResponse('About page')