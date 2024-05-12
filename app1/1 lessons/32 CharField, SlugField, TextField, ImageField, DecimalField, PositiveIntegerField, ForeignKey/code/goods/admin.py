from django.contrib import admin
# 1) Admin panelde gorsenmesi ucun PRODUCT cedvelini qeydiyyata saliriq.
from goods.models import Categories, Products

admin.site.register(Categories)
admin.site.register(Products)



# 2) Ve terminalda tekrar yaziriq:
#       a) python manage.py makemigrations
#       b) python manage.py migrate


# 3) Birinci komandani yazdiqda, MODELS.PY faylinda olan ImageField() metoduna gore PILLOW xetasi alasiyiq. Bunu duzeltmek ucun bele yaziriq: pip install Pillow

