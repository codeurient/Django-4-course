# 1) Bu CLASS icinde hec bir deyisiklik etmeyeceyik.
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
    ]


# 2) Indi ise serveri işə salsaq termianlda belə bir mesaj görəcəyik:   You have 1 unapplied migration(s).....

# 3) Bu xeta mesaji evvel aldigimiz 18 migrate xeta mesaji ile eynidir. Yəni, cədvəli DB-sə MİGRATE etmək lazım olduğunu bizə bildirir:  python manage.py migrate



# 4) Əgər MİGRATE etdikdə hər hansısa bir xəta baş verərsə yaxud cədvələ sonrada yeni bir şeylər əlavə etmək istəyəriksə, yaxud DB.SQLİTE3 faylı silinərsə, biz proqramı
# F5 edərək təkrar işə saldıqda DJANGO bu proqramı təkrar yaradacaq və yenidən belə bir xəta mesajı göstərəcək: You have 19 unapplied migration(s)...

# 5) Ilk once, GOODS/MIGRATIONS qovlugunda yaranan "0001_initial.py" adli fayli silir. Bunlari ederek proqramin işini dayandirmış olmalıyıq. 
# 6) 




# Default olaraq DJANGO cədvəli yaradarkən ona bu cür ad verrir: qovlugun adı GOODS, altdan xətt _ sonra isə CLASS-ın adı:   goods_categories
# İstəsək bunu dəyişdirə və özümüz istəyən adı qoya bilərik. Bunun üçün CATEGORİES klası içində başqa bir klass yaratmalıyıq: 
        # class Meta:
        #      db_table = 'category'           - adı cəmdə yox təkdə yaradırıq. Yəni categories yox category