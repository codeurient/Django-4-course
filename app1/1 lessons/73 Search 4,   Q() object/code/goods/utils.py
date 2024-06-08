# 1) Məhsulu açar sözlərdən istifadə edərək filter-ləmək üçün 'Q' deyilən bir obyekt var və onu İMPORT etmək lazımdır. Gəlin ilk öncə TERMİNALDA baxaq görək nədir bu 'Q' obyekt və nə verir bizə.

# 2) Bunun üçün DEBUG TOOLBAR-ından istifadə edə bilərik:  python manage.py debugsqlshell

# 3) Sonra lazımlı İMPORT-ları terminalda təkrar yazırıq ve UZUN bir kod ilə, məhsulu açar sözdən istifadə edərək filter-ləyirik ki, həmin məhsulu əldə edə bilək:
#                                                                                                                                               Products.objects.filter(price__lt=50) | Products.objects.filter(description__contains='table')
# Bu kod çox uzun olduğundan istifadəsi də yorucudur. Bunun üçündə 'Q' deyilən obyektdən istifadə edilir:                                       Products.objects.filter(Q(name__contains='table') | Q(description__contains='table')) 
from django.db.models import Q

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    # 5) SPLIT() metodu STRING-ləri müəyyən edilən simvoldan-simvola bölmək üçün istifadə edilir. Əgər simvol təyin etməsək DEFAULT olaraq SPACE simvolu nəzərdə tutulacaqdır. SPLIT() metodu LIST qaytarir. Bizdə FOR ilə LİST içindən
    #    tək-tək dəyərləri əldə edirik. 
    # 
    #    cumle = "This is a test"
    #    bolunmusSozler = cumle.split()
    #    print(bolunmusSozler)          # Netice: ['This', 'is', 'a', 'test']
    # 
    #    1ci olaraq kodun bu hissesi isleyir:   for word in query.split()              query.split()-de olan deyerler 'word' adli variable-a gonderilir. 
    #    2ci olaraq kodun bu hissesi isleyir:   if len(word) > 2                       hemin 'word' variable-inda olan deyerler if ilə muqayise edilir.
    #    3cu olaraq kodun bu hissesi isleyir:   word.                                  Muqayiseden sonra deyerler en basdaki 'word' adlı variable-a gonderilir.
    # 
    keywords = [ word for word in query.split() if len(word) > 2 ]
    # 6) Nəticə olaraq 'KEYWORDS' adlı variable-a LİST tipini həmin dəyərlər ilə yerləşdiririk:     keywords = ['this', 'test']

    # 7) 'Q_OBJECTS' variable-na  Q()  obyektini veririk. 
    q_objects = Q()

    # 8) For ilə 'KEYWORDS' list-inden deyerleri tek-tek elde ederek TOKEN variable-ina veririk ki,  Q() obyekti vasitesi ile, CEDVELIN sütununda bu dəyəri axtaraq:    Q(description__icontains=token)  
    for token in keywords:
        # 9) |=   bu  simvol  ilə  bütün  Q()  obyektlərini birləşdiririk çünki sorğu birdən çox ola bilər. Məsələn Title-da olan dəyər ilə yaxud Description-da olan dəyər ilə mıhsul axtarıla bilər. 
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    # 9) Sonra isə FİLTER() metodu ilə axtarışı həyata keçiririk. 
    return Products.objects.filter(q_objects)