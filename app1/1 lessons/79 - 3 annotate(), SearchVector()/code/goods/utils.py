from django.db.models import Q
# 2)
from django.contrib.postgres.search import SearchVector
from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
# 1)Eyni vaxtda həm NAME həm DESCRİPTİON üzrə axtarış etmək istəyiriksə onda, DJANGO-nun ANNOTATE() metodundan istifadə edərək QuerySet-ə birdən çox sahə əlavə edə bilərik:  https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/search
    return Products.objects.annotate(
                                      search=SearchVector("name", "description"),
                                    ).filter(search=query)
# 2) SearchVector() klası SEARCH adlı variable-a həm 'NAME' həm 'DESCRIPTION' adlı sahələri ayrı ayrı verəcək. Sonra isə bu SEARCH variable-ına FİLTER() metodu ilə sorğunu göndəririk. 