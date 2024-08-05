from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/',          views.login,            name='login'),
    path('registration/',   views.registration,     name='registration'),
    path('profile/',        views.profile,          name='profile'),
    # 1) Sayta daxil olan istifadəçinin öz səbətinə daxil olması üçün ayrıca səbətə keçid URL-si yaradırıq.  Sonra daxil oluruq USERS controller-inə ki, 
    #    USERS_CART() metodunuda əlavə edək ki, həmin metod vasitəsi ilə USERS qovluğundakı USERS_CART.HTML faylını aça bilək. 
    path('users-cart/',     views.users_cart,       name='users-cart'),
    path('logout/',         views.logout,           name='logout'),
]


