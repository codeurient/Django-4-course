from django.db.models import Q
# 2)
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, SearchHeadline
from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

# 1) SearchHeadline() klası ilə SEARCH sahəsində yazılan sözü TAG içinə yerləşdirərək həmin sözün vurğulanmasını yəni ayrıca işarətlənməsini söyləyə bilərik. Bunun üçün ilk öncə SEARCH sahəsində
#    axtarışa verilən sözün nəticəsini yerləşdiririk RESULT adlı variable-a. 
    result = Products.objects.annotate(
                                        rank=SearchRank(vector, query)
                                    ).filter(rank__gt = 0).order_by("-rank")

# 2) Sonra yenə ANNOTATE() metodu ilə bu nəticəyə açıxlama əlavə edirik. Əlavə edilən açıxlama SearchHeadline() klası ilə SEARCH sahəsində yazılacaq sözün <span> tag-i içinə yerləşdirilməsidir.
    result = result.annotate(
        # 3) Normalda məhsulun adını əldə etmək üçün PRODUCT.NAME yazırıq ŞABLONDA-da ancaq eyni adın SearchHeadline() klası ilə işarətlənmiş yeni versiyasını əldə etmək üçün PRODUCT.HEADLİNE yaza bilərik.
        #    Çünki, nəticəni həmin HEADLİNE adlı variable içinə yerləşdiririk. 
        headline = SearchHeadline( 'name',            query,      start_sel = '<span style="background-color: yellow;">',       stop_sel='</span>', )
    )

    result = result.annotate(
        # 4) Həmçinin DESCRİPTİON sahəsinidə əldə etmək üçün PRODUCT.DESCRİPTİON yazırıq ŞABLONDA-da ancaq eyni mətnin SearchHeadline() klası ilə işarətlənmiş yeni versiyasını əldə etmək üçün PRODUCT.BODYLİNE yaza bilərik.
        bodyline = SearchHeadline( 'description',     query,      start_sel = '<span style="background-color: yellow;">',       stop_sel='</span>', )
    )

# 5) Nəticəni RETURN edərək gedirik şablona.
    return result

