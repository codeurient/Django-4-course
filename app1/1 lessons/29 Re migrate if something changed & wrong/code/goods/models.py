from django.db import models

class Categories(models.Model):

    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    # 3) Default olaraq DJANGO, table yaradarkən ona bu cür ad verrir: qovlugun adı GOODS, altdan xətt _ sonra isə CLASS-ın adı:        goods_categories
    # İstəsək bunu dəyişdirə və özümüz istəyən adı qoya bilərik. Bunun üçün CATEGORİES klası içində başqa bir klass yaratmalıyıq.
    class Meta:
        db_table = 'category'           # adı cəmdə yox təkdə yaradırıq. Yəni 'categories' yox 'category'

        # 4) Sonra terminalda evvel yazdigimiz kamandani yaziriq:       python manage.py makemigrations
        # 5) Sonra ise table-i migrate edirik:                          python manage.py migrate




        


# 1) Əgər MİGRATE etdikdə hər hansısa bir xəta baş verərsə yaxud cədvələ sonradan yeni bir şeylər əlavə etmək istəyəriksə, yaxud DB.SQLİTE3 faylı silinərsə və.s, birincisi biz proqramı
#    F5 edərək təkrar işə saldıqda DJANGO bu DB.SQLİTE3 faylini təkrar yaradacaq və yenidən belə bir xəta mesajı göstərəcək: You have 19 unapplied migration(s)...

# 2) Ilk once, proqramin işini dayandiririq sonra ise GOODS/MIGRATIONS qovlugunda yaranan "0001_initial.py" adli fayli silirik ve etmek istediyimiz deyisikliyi GOODS/MODELS.PY faylina yaziriq.