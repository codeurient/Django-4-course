from django.db.models import Q
# 2)
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    # 1) Burada esas lazim olan class SearchRank()-dır. Bu klas axtarış vaxtı İNPUT sahəsində bir yazı yazdıqda, nəticəni ən məntiqli nəticəyə görə ən üstdə göstərmək üçün istifadə edillir. 
    #    Yəni, bir sorğunun DB-də axtarılan məlumat ilə nə qədər əlaqədar olduğunu qiymətləndirir və ORDER_BY() ilə istifadə edilərək ən məntiqli, ən əlaqədar olan nəticələri ən birinci sırada
    #    göstərmək üçün istifadə edilir.
    return Products.objects.annotate(
                                        rank=SearchRank(vector, query)
                                    ).filter(rank__gt = 0).order_by("-rank")

    # Hal-hazirda bu kod tam deqiq islemeyecek. Proqramı işə salaraq gedib saytda SEARCH sahəsində bir şeylər yazsaq görərik ki, ilk öncə axtardığımız
    # məhsullar qarşımıza çıxacaq sonra isə bütün digər məhsullar. Bunun səbəbini daha rahat başa düşmək üçün kodun bizə nə verdiyinə DEBUGSQLSHELL ilə
    # terminal pəncərədə baxaq. Bunun üçün terminalda belə yazırıq:
    #                                                               In [1]: from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

    #                                                               In [2]: from goods.models import Products

    #                                                               In [3]: from goods.utils import q_search

    #                                                               In [4]: x = q_search('table')

    #                                                               In [5]: for i in x:
    #                                                               ...:     print(i.rank)
    #                                                               ...:     print(i.name)
    #                                                               ...: 

    # Nəticə olaraq SearchRank() metodunun, axtarılan sözə görə hər məhsulu necə qiymətləndirdiyini görəcəyik. Məsələn:  0.075990885 -dan 0-a qədər. 
    # 'NAME' bizim özümüzn cədvəlində olan SÜTUN adıdır. RANK isə hər məhsul üçün SearchRank() metodunun yaratdığı SÜTUN adıdır. Bu sütunda hər məhsul üçün SearchRank() metodunun təyin etdiyi
    # qiymət olacaq. Bizdə, 0 (sıfır) olanları görməyək deyə FİLTER() metodundan və __GT lookup-ından istifadə etməliyik. __GT (greater than) demekdir. Yuxarıda ki, koda FİLTER metodunu bu cür 
    # əlavə edəcəyik:
    #                    return Products.objects.annotate( rank=SearchRank(vector, query) )                     .order_by("-rank")
    #                    return Products.objects.annotate( rank=SearchRank(vector, query) ).filter(rank__gt = 0).order_by("-rank")