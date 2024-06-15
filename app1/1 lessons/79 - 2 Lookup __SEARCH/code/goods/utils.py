from django.db.models import Q

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    # 1) Əvvəl yazdığımız balaca kodu kommentə alırıq və DJANGO-nun daxili alqoritmasından istifadə edərək həmin kodun eynisini yazırıq axtarış etmək üçün.
    #    Burda '__search' lookup-ından istifadə etmişik. Lookup-lardan, DJANGO ORM-də, müəyyən bir sahəyə əsaslanan sorğular yaratmaq üçün istifadə olunur. DJANGO-nun __search lookup-ı,
    #    Tam Mətn Axtarışı (Full-Text Search (FTS)) həyata keçirmək üçün istifadə olunur. Yəni, bu LOOKUP sahəyə yazdığımız məzmunu axtarır və həmin məzmuna uyğun gələn nəticəni bizə göstərir.
    #    Bu LOOKUP-ın istifadəsi sadədə POSTGRESQL db-si üçün keçərlidir. 
    return Products.objects.filter(description__search=query)
    # 2) QUERY parametri bizim INPUT sahesine yazdigimiz yazidir ve hemin yazi DESCRIPTION sahesinde __SEARCH edilsin deyirik.  

    # 3) ICONTAINS ve DJANGO daxili alqoritmasi ilə axtardıqda olan aradakı fərqlər nələrdir ? 
    #                                                                                           a) İCONTAİNS alqoritmasi sadəcə, sözün yaxud hərfin həmin TİTLE yaxud DESCRİPTİON içində olub olmadığına baxır. Yəni 's' hərfi yazdıqda
    #                                                                                              bu 'set' sözündə 's' hərfi olduğu üçün uyğun gələn məhsulu əldə edəcəyik. 
    # 
    #                                                                                           b) DJANGO daxili alqoritmasi isə bu cür 's' hərfi yazdıqda 'set' sözündə 's' hərfi olsa belə həmin məhsulu göstərməyəcək. Çünki DJNAGO
    #                                                                                              daxili alqoritması, axtarılan söz ilə həmin mətndə mövcud olan söz arasındakı BƏNZƏRLİYİ nəzərə alaraq axtarış edir. Yəni, bu söz neçə
    #                                                                                              faiz bənzərliklə mövcuddur. Belə axtarış etmək bizə dəqiq nəticə əldə etməyə kömək edir. (Sözlərin oxşarlığının faiz ehtimalı)
    # 



    
    
    # keywords = [ word for word in query.split() if len(word) > 2 ]
    # q_objects = Q()
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    # return Products.objects.filter(q_objects)