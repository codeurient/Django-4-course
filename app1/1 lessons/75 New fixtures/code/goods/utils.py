from django.db.models import Q

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [ word for word in query.split() if len(word) > 2 ]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects)


# 1) FİXTURES qovlugunun içindən CATS.JSON və PROD.JSON fayllarını silirik. 

# 2) Sonra TERMİNAL pəncərəni açaraq bu kamandanı daxil edirik və ENTER-ə basırıq:   python manage.py dumpdata goods.Categories > fixtures/goods/categories.json
#                                                                                    python manage.py dumpdata goods.Products > fixtures/goods/products.json

# Bu kamanda categories.json və products.json adında fayl yaradaraq Cədvəldən məlumatları götürərək həmin JSON fayllarını dolduracaq. 

# Bu kamandalardan sonra DB.SQLİTE3 faylını silə bilərik. 