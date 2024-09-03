from django import template

from carts.models import Cart
from carts.utils import get_user_carts


register = template.Library()

@register.simple_tag()
def user_carts(request):
    # 1) Sonra bu faylın içində UTİLS.PY faylında yaratdığımız      GET_USER_CARTS()    metodunu import edərək RETURN edirik.  Sonra isə bu funksiyanı 
    return get_user_carts(request)


