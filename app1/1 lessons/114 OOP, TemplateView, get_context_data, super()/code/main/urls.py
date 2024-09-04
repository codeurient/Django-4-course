from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    # 1) CLASS -ın adını yazırıq və  as_view()  metodu ilə şablon kimi qəbul edirik deyirik həmin class-ı. 
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
]