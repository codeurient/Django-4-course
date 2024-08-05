from django import template

from carts.models import Cart


register = template.Library()

@register.simple_tag()
# 1) REQUEST  parametrinde USER parametri movcud oldugu ucun   REQUEST.USER   yazaraq hal-hazirki istifadecini cagira ve CARTS modelinin USER sutunundaki deyer ile eynilesdirib FILTER()-leyerek, sayta giriş edən istifadəçinin
#    hemin sebete elave edilen mehsullarını elde edirik.
def user_carts(request):
    # 2) Bu funskiyanı çağırdıqda, nəticə olaraq QUERYSET bizə RETURN edəcək. Deməli aşağıda göstərilən fayla daxil olduqda bu funksiyanın adını yazacağıq və həmin funksiya işə keşəcək,
    #    Sonra parametr olaraq REQUEST ötürüləcək bu funksiyaya və nəticə olaraq QUERYSET qayıdacaq. Qayıdan QUERYSET nəticəsinidə verəcəyik CARTS adlı başqa parametrəyə ki istifadə edək:
    #                                                                                                                                                                                           {% user_carts request as carts %}
    #                                                                                                                                                                                          
    #    NOT:  user_carts( ) metodunda qeyd edilen REQUEST parametri INCLUDED_CART.HTML faylında bu metodu çağırdığımız zaman göndərilən REQUEST sorğularını ehtiva edir: user, post, get, session, meta və.s 
    #    Yəni ilk öncə INCLUDED_CART.HTML faylı ilə sorğu göndəririk sonra CARTS_TAGS.PY faylında onu qarşılayırıq.
    return Cart.objects.filter(user=request.user)



# 3) Indi funksiyani çağırmaq üçün daxil oluruq          CARTS / TEMPLATES / CARTS / INCLUDES / INCLUDES_CART.HTML        faylına


# 4) Django şablon taglərini istifadə edərək şablonlarda tekrar-tekrar istifadə edə biləcəyimiz məzmunlar yarada bilərik. 

