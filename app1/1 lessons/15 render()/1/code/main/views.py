from django.http import HttpResponse
from django.shortcuts import render

# 1) 'Home page' adli string evezin HTML şablon RENDER etmek ucun, MAIN qovlugu icinde TEMPLATES (mutleq bu adda olmalidir) adinda qovluq yaratmaq lazimdir.
# Birden cox TEMPLATES adinda qovlugumuz ve her birinde INDEX.HTML faylimiz olacaq. Hal-hazirda biz ana sehifeni render etmek isteyirik. Ancaq
# proyekt boyudukce DJANGO, templates qovluqlarini ve index fayllarini qarisdira biler. Bunun olmamasi ucun TEMPLATES qovlugunun icinde de, render edilen
# sehifinin adini yazmaq meslehetdir. Hemin qovluq icinde de INDEX.HHTML faylini yaradiriq.
def index(request) -> HttpResponse:
    # 2) Nece edek ki, hemin fayli CONTROLLER-e qosaq. Bunun ucun RENDER() metodundan istifade edirik. Hemin metodun icinde 1ci parametr olaraq REQUEST,
    # ikinci parametr olaraq sablonu yaziriq. DNAJGO avtomatik olaraq TEMPLATES qovlugunu gorduyunden onun adini yazmaq lazim deyil. Bir basa MAIN ve faylin 
    # adini yazmaq kifayetdir.
    return render(request, 'main/index.html')




def about(request):
    return HttpResponse('About page')