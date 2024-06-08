from goods.models import Products


def q_search(query):
    # 1) IF ilə sorğu yaradırıq ki, QUERY parametrinin dəyəri rəqəmsaldırsa və daxil edilən 5 simvoldan azdırsa PRODUCTS cədvəlindən həmin İD-yə uyğun gələn məhsulu tapaq.
    if query.isdigit() and len(query) <= 5:
        # 2) SEARCH sahəsinə daxil edilən dəyər FİLTER() metodu vasitəsi ilə PRODUCTS cədvəlinin İD-si ilə eyniləşdirildikdən sonra bu İD-yə uyğun gələn məhsul əldə edilir.
        # Cədvəldə 5 var ancaq 00005 yoxdur. Necə olur ki, SEARCH sahəsinə 00005 yazdıqda məhsulu əldə edə bilirik ? Çünki, İNT() metodu gərəksiz 0 (sıfırları) silir.
        return Products.objects.filter(id=int(query))
    
    # 3) Nə üçün GET() əvəzinə FİLTER() metodundan istifadə edirik ? Çünki GET() metodundan istifadə etdikdə MƏHSUL-u əldə edirik ancaq bizə QUERYSET tipinin qayıtmağı lazımdır. 
    # Çünki GOODS/VIEWS.PY faylında QUERYSET metodlarından istifadə etmişik. 