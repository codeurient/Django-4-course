from django import template
# 2) 'urlencode' IMPORT edildi. 
from django.utils.http import urlencode
from goods.models import Categories

register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


# 1) 50 nomreli dersde TEMPLATE.LIBRARY(), SIMPLE_TAG ve.s haqqinda demişdik. Bunlar @REGİSTER.SİMPLE_TAG() dekaratorunu istifadə edərək CHANGE_PARAMS() funksiyasını ŞABLON TAG-i kimi istifadə etməyimizə imkan yaradır. 
#    Şablon tag-ləri DJANGO şablonunda təkrar təkrar istifadə edilə bilir. Bu DECORATOR-da bir Python funksiyasını Django şablon matoruna Şablon tag-i kimi tanıdaraq, şablonlarda istifadə edilməsinə köməklik yaradır. 
#
# 2) TAKES_CONTEXT parametri onu bildirir ki, bütün CONTEXT dəyişkənlərini əldə etmək istəyirik. CONTEXT dəyişkənləri yerləşir GOODS/VIEWS.PY faylının içində:
#                                                                                                                                                               title
#                                                                                                                                                               goods
#                                                                                                                                                               slug_url
#                                                                                                                                                               request  ve.s 
# 
# Nə vaxtki, biz ŞABLONDA CHANGE_PARAMS() funskiyasını çağırırıq onda, bu funksiya avtomatik olaraq həmin CONTEXT dəyişkənlərini qəbul edir və ötürür bu funksiyanın CONTEXT parametrinə 
@register.simple_tag(takes_context = True)
def change_params(context, **kwargs):
    # 3) CONTEXT parametri içində bütün CONTEXT dəyişkənləri olduğundan biz bizə lazım olan REQUEST açar sözü ilə HTTP sorğusundan gələn dəyərləri ildə edirik:     on_sale=on  &  order_by=price
    # DICT() metodundan istifadə etmə məqsədimiz əldə edilən dəyərlərin QueryDict tipində olmağıdır. Bizdə bu QueryDict tipini normal Python Dict tipinə çeviririk. 
    query = context['request'].GET.dict()
    # 4) CHANGE_PARAMS() funksiyasında olan 2ci parametr KWARGS isə ŞABLON-dan bizim manual olaraq göndərdiyimiz açar söz və dəyərlərdir (page=page) olan hissə:           <a  href="?{% change_params page=page %}">{{ page }}</a>
    # 5) KWARGS parametrində olan DİCT ilə QUERY variable-ında olan DİCT-i yeniləyirik. Yəni QUERY dict-inə KWARGS dict-ini əlavə edirik. Belə olduqda nə köhnə sorğu parametrləri itəcək nə yeni. 
    query.update(kwargs)
    # 6) URLENCODE() metodu isə DİCT tipinin açar söz və dəyərlərini URL sətirinə çevirir. Meselen:
    #                                                                                               params = {
    #                                                                                                   'page': 2,
    #                                                                                                   'category': 'fruits and vegetables',
    #                                                                                                   'sort': 'name asc'
    #                                                                                               }
    #                                                                                               encoded_params = urlencode(params)
    #                                                                                               print(encoded_params)   
    # 
    #                                                                                               Netice:  page=2&category=fruits+and+vegetables&sort=name+asc
    return urlencode(query)