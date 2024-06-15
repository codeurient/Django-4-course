from django.db.models import Q

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [ word for word in query.split() if len(word) > 2 ]

    q_objects = Q()

    for token in keywords:
        # 1) Fikir vermişdinizsə biz burda axtarış etmək üçün CONTAİNS əvəzinə İCONTAİNS istifadə etmişik. İ sözü kiçik və böyük hərf fərqi qoymadan axtarış et mənasına gəlir. 
        #    SQLite -da bu ICONTAINS işləmədiyi üçün yazmamışdıq. Ancaq POSTGRESQL-də işləyidi üçün bundan istifadə etmişik. 
        #    
        # 2)  Bizim burda istifadə etdiyimiz alqaritm tam mətn axtarışıdır. Yəni həm TİTLE həmdə DESCRİPTİON da olan mətnə görə axtarış edirik. Bu qeyri peşəkar yanaşmadır. 
        #     Ancaq, DJANGO-nun daxilində onu özünün tam mətn axtarışı həyata keçirmək üçün olan daxili dəstəyi mövcuddur.. Gəlin bunu realizasiya edək. Daxil olmalıyıq APP/SETTINGS.PY faylına.

        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects)