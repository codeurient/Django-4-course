from django.contrib import admin

# 1) 30 nomreli dersde olan Admin panele baxdiqda goruruk ki, orda 2 dene table var ancaq bizim yaratmis oldugumuz CATEGORY table-i yoxdur cunki onu qeydiyyata salmamisiq. 
# Category cedvelini qeydiyyata salmaq ucun GOODS/ADMIN.PY  faylinda asagidaki kodlari yaziriq:

# 2) Ilk once MODEL-imizi IMPORT edirik. 
from goods.models import Categories

admin.site.register(Categories)


# 3) ADMİN.PY faylında yaza bilerik ki, nəyi gosterek admin panelde, nələri dəyişə bilək nələri yox ve.s. Ancaq bunlari sonra edeceyik. 


# 4) Modelin adı olan CATEGORIES cemde oldugu ucun Admin panele elave edilyinde sonuna avtomatik olaraq bir 'S' herfi daha elave edilir. Bunu deyisdirmek mumkundur. 
# Elave olaraq qeyd edim ki, admin panelin dilide default olaraq ingilis dilindedir ve bunuda deyisdirmek mumkundur. Bunun ucun asagidaki addimlari izleyek:
#
#   a) APP/SETTINGS.PY faylini aciriq. 
#   b) Hemin faylin icinde: LANGUAGE_CODE = 'en-us'   bele bir deyisken goreceyik ve 'en-us' yazisini meselen 'az' ile evez edirik ve admin panel Azerbaycan dilinde olacaqdir.
# 
# Ancaq Azerbaycan dili cox taninan ve desteklenen bir dil olmadigi ucun bezi yazilar ingilis dilinde qala biler.
# Ve birde Ingilis dilinde qalan hisse o hisseler olacaq ki, hansilariki biz ozumuz Manul elave edirik. Elə bunun üçündə həmin adları Manul dəyişdirmək lazımdır. 
# Bunun ucun gedirik GOODS/MODELS.PY faylına.