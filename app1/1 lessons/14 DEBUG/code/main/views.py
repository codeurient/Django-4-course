from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    return HttpResponse('Home page')






def about(request):
# 1) F5 duymesini basaraq proqrami işə saliriq. Sonra VSC-de sol terefde reqemler olan yerde RETURN-un onune qirmizi daire ile isare qoyuru ve brauzere 
# kecid ederek sehifeni yenileyirik. Bu zaman REQUEST parametrinin ne qaytardigini DEBUG penceresinde gore bileceyik. Cookiler, butun istifadeci melumatlari
# ve.s hemin REQUEST parametri ile bize geri qayidir.
    return HttpResponse('About page')

# 2) DEBUG rejiminden cixis etmek ucun terminali qapada yaxud sag yuxarida olan olan balaca penceredeki play kimi gorunen duymeni klikleyerek DEBUG
# rejiminden cixmaq olar.