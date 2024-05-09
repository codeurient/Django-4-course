from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    
    context = {
        'title' : 'Home',
        'content' : 'Home page of magazines - HOME',
        'list' : ['first', 'second'],
        'dict' : {'first': 1},
        # 1) Bool acar sozunu deyisdirdik.
        'is_authenticated' : True
    }

    return render(request, 'main/index.html', context)




def about(request):
    return HttpResponse('About page')