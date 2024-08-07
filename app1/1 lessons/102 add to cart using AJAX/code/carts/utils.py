from carts.models import Cart


# 1) CARTS_TAGS.PY faylındakı USER_CARTS() metodunun içində əvvəl yazdığımız kodları kəsərək götürürük və UTİLS.PY faylına yerləşdiririk. 
def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)