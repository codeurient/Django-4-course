from django.db.models import Q

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [ word for word in query.split() if len(word) > 2 ]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects)

# 1) Serverde sorgular ile daha effektiv islemek ucun SQLite evezine PostgreSQL -den istifade etmek mesheletdir. POSTGRESQL verilenler bazasini idare etmek ucun istifade edilen sistemidir. 
# Bunun ucun PostgreSQL quraşdırmaq lazımdır: https://www.postgresql.org/

# a) sayta daxil oluruq
# b) uygun versiyani axtaririq. Django ve Python ile uygun gelen versiyani oyrenmek ucun gosterilen sayta kecid edirik: https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes
# c) PostgreSQL notes hissesinde yazilibdir hansi versiya uygun versiyadir deye: Django supports PostgreSQL 12 and higher. En son versiyani yukleyirik.
# d) PostgreSQL-in 12 versiyasindan yuxari olan istenilen versiyasini qurasdira bilerik.
# e) PostgreSQL ile islemek ucun elave 2 paketden birisini de yuklemek lazimdir:  psycopg  yaxud   psycopg2 

# f) Indi endirek ve proqrami acaraq qurasdiraq: Burda Next ederek gedirik ve sonra bizden soruşacaq ki, Cədvəli harda saxlamaq istəyirsiz ? Cədvəlin saxlanıldığı yeri deyisdire bilersiz. 
# Windows-da bir yer secin ozunuze ve DATABASEPLACE adında qovluq yaradaraq həmin qovluqda yadda saxlayacağıq deyin Cədvəli. 
# g) Sonra NEXT deyirik ve parol daxil edin teleb edilecek. Burda men 'root' yaziram qisaca. 
# h) Port-a deymirik ve NEXT deyirik. 
# i) Local-ı DEFAULT olaraq saxlayiriq ve NEXT NEXT NEXT NEXT deyirik. 
# j) Stack Builder yazinin önündən işarəni qaldıraraq FİNİSH deyirik. 



# 2) POSTGRESQL-i quraşdırdıqdan sonra proyekti hal-hazırki DB-dən yeni DB-ə keçirmək lazımdır. Bu o demekdir yeni FİXTURES yaratmalıyıq. Bizim FİXTURE-imiz artıq movcuddur. 