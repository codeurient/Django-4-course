from django.apps import AppConfig


class GoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goods'
    # 1) Əgər 3 nömrəli şəkildə qırmızı ilə işarələnən başlıq yazısını dəyişdirmək istəyiriksə onda, bunu GOODS/APPS.PY faylında etməliyik. 
    verbose_name = 'Mehsul'