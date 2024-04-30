# 4) Proqram avtomatik olaraq funksiyani IMPORT etdi.
from django.http import HttpResponse
# 1) RENDER ne demedkir ? Melumatlarin istifadeci interfeysine (brauzere) gonderilmesine render etmek deyilir.
from django.shortcuts import render

# Create your views here.


# 2) Ilk once 'INDEX' adinda funksiya yaziriq hansi ki, bu funksiya istifadecilerden gelen sorgunu işləyəcək. 
# Sorgunu REQUES adli parametri qebul edecek. Hemin parametr, HTTP REQUEST CLASS-inin nusxesini ozunde ehtiva edecek.
# Hemin CLASS nusxesi sorgu haqqinda movcud olan butun melumatlari ehate edir. Meselen: Giris eden istifadeci 
# qeydiyyatdan kecibdirmi yoxsa anonimdirmi, get, post ve.s
def index(request) -> HttpResponse:
    # 3) Request geldikden sonra bizde avtomatik olaraq geriye RESPONSE gonderirik. Bunun ucun HTTPRESPONSE() funskiyasini RETURN edirik.
    # Meselen, sorgu olaraq hemin funksiyasinin icinde bir kontekt gondere bilerik. DJANGO-da, VIEWS.PY faylinda yazilan bu cur funksiyalar 
    # eslinde CONTROLLER yaxud VIEW adlanir. Yəni, termin olaraq funksiya evezine çox vaxt controller yaxud view deyirler.
    return HttpResponse('Home page')


# 5) Controlleri yaratdiqdan sonra onu ucun URL adres teyin etmeliyik. Bunu 'APP/URLS.PY' faylinda edirik. Gedirik hemin fayla ve
# controller-imizi qeydiyyata aliriq. 







# 6) Test meqsedli ikinci URL adreside elave edek ve sonra brauzere kecerek URL yerinde yazaq:  http://127.0.0.1:8000/about/
def about(request):
    return HttpResponse('About page')