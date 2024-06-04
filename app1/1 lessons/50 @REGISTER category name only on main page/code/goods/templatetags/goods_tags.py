# 1) Django paketlerinin icinden TEMPLATE adli alt paketi IMPORT edirik ki, ŞABLON TAG-imizi (tag_categories) qeydiyyata salaq.
from django import template


from goods.models import Categories


# 2) REGISTER adinda bir variable yaradiriq. Bu variable-a TEMPLATE paketinin içindən çağırdığımız LİBRARY() class-ını veririk. 
register = template.Library()

# 3) Sonra isə xüsusi DEKARATOR olan @ simvolu ilə bu variable-ı qeydiyyata salırıq. 
@register.simple_tag()


# 4) Artıq   'TAG_CATEGORİES()'   adından istifadə edərək həmin funksiyanı ŞABLON içində çağıra bilərik. Funksiya isə DB-dən bizim üçün kateqori adlarını RETURN edəsidi. 
def tag_categories():
    return Categories.objects.all()