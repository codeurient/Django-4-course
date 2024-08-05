from django.apps import AppConfig


class CartsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carts'

    # 1) Admin paneldə tətbiqin necə adlanacağını qeyd edirik.
    verbose_name = 'Carts'

    # 2) Sonra terminala daxil olaraq miqrasiyani işə salırıq:
    #                                                         a) python manage.py makemigrations
    #                                                         b) python manage.py migrate

    # 3) Indi isə məhsulun səbətə əlavə edilməsi funksionallığını yarada bilərik. Ancaq ilk öncə bir balaca dəyişiklik edək   CART / VIEWS.PY     və     CARt / URLS.PY    faylında 
    #     product_id    parametrini     product_slug   ilə əvəzləyək. 



    # 4) Sonra daxil olasıyıq GOODS / TEMPLATES / GOODS / PRODUCTS.HTML faylına ki, məhsulun yanında səbət ikonu var. Bu ikon A tag-indir. Bizdə bu A tag-inə URL veririk ki,
    #    həmin ikon klikləndikdə CART_ADD metodu işləyərək seçilən məhsul səbətə əlavə edilsin. 