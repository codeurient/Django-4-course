from django.http import HttpResponse
from django.shortcuts import render

# 1) 

def index(request) -> HttpResponse:
    # 2) 

    context = {
        'title' : 'Home - main',
        'content' : 'Furniture store HOME',
        # 3) 

    }
    return render(request, 'main/index.html', context)



def about(request):
    context = {
        'title' : 'Home - about',
        'content' : 'Here is some text about us',
        'text_on_page': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ',
    }
    return render(request, 'main/about.html', context)




#! 4)  CATEGORY adlarini ekrana yazdirmaq üçün     MAİN/TEMPLATES/MAİN/BASE.HTML     faylında İF şablon tag-indən istifadə etmişik. 

# <ul>
#     {% for category in categories %}
#         <li><a  href="{% url "catalog:index" %}">{{ category.name }}</a></li>
#     {% endfor %}      
# </ul>

#! Bu yazıların digər səhifələrdə görsənməməsinin səbəbi həmin CATEGORY variable-ını yuxarıdakı İNDEX() funksiyasının içində yazmaqdır. 
#! Çünki İNDEX() funksiyası SADƏCƏ ana səhifədir. 

#! BASE.HTML faylı isə bütün səhifələr üçün eynidir.   Burda diqqət etmək gərəkən yer, əgər BASE faylı bütün səhifələr üçün eynidirsə onda gərək İF şablon tag-idə BASE faylında
#! olduğu üçün təkrarlanmalı idi deyə düşünə bilərik. Ancaq dedik ki, bunun səbəbi İF şablon tag-inin İNDEX() funksiyasında yazılmasıdır. İNDEX() isə sadəcə 1 səhifədir. ANA səhifə !!!