from django.db import models

class Categories(models.Model):

    # 4) İnput sahelerin onunde duran yazini deyisdirmek ucun de CharField() metodunun 'verbose_name'  parametrinden istifade etmek olar.
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'               # 1) Burda yazdigimiz CATEGORY sozu DB-de hemin cedvelin adinin ne forma gorseneceyini teyin etmek ucundur dedik.
        verbose_name = 'Category'           # 2) ADMIN PANEL-de nece gorseneceyini nece teyin etmek ucun ise xususi VARIABLE olan VERBOS_NAME-den istifade edirik. Istenilen dilde olar.
        verbose_name_plural = 'Categories'  # 3) verbose_name deyiskeninde yazilan DEYER tekde,  verbose_name_plural deyiskeninde yazilan DEYER cemde olmalidir. 