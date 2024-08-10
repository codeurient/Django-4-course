from carts.models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    
    # 1) Əgər istifadəçi qeydiyyatdan keçməyibdirsə onda onun üçün burada SESSİON KEY təyin edəcəyik. If ilə deyirik ki, əgər SESSİON KEY yoxdursa onda CREATE et. 
    if not request.session.session_key:
        request.session.create()
    # Əgər SESSİON KEY varsa onda, İF FALSE verəcək və kod bizə mövcud SESSİON KEY ilə əlavə edilən məhsulu RETURN edəcək.
    return Cart.objects.filter(session_key=request.session.session_key)


# 2) Proqramı işə salırıq və sayta giriş etmədən səbətə məhsul əlavə etməyə çalışıq. Məhsul əlavə ediləcək ancaq sayta giriş etsək onda SESSİON KEY dəyişəcək və əlavə edilən məhsullar itəcək
#    Saytdan cixis etdikde artiq sebetde mehsul gormeyeceyik. Ancaq DB-de (Admin panelde sadece daxil olduqda xeta verecek) silinmesine baxmayaraq bu mehsul olacaq. 

#    Elə etmək lazımdır ki, istifadəçi sayta giriş etmədən səbətə məhsul əlavə etdikdə və sonra sayta giriş etdikdə  yaxud qeydiyyatdan keçdik bu məhsullar itməsin və session-lardan ötürülsün
#    giriş etmiş istifadəçinin hesabına. 


# 3) Ilk öncə daxil oluruq      USERS / VIEWS.PY      faylına.  Çünki İstifadəçi ilə SESSİON KEY arasında əlaqə yaratmaq lazımdır. 


