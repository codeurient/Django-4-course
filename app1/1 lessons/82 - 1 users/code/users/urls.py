from django.urls import path

# 1)
from users import views

# 2)
app_name = 'users'

urlpatterns = [
    # 3) Bizə lazım olacaq marşrutları əlavə edirik. 
    path('login/',          views.login,            name='login'),
    path('registration/',   views.registration,     name='registration'),
    path('profile/',        views.profile,          name='profile'),
    path('logout/',         views.logout,           name='logout'),
]