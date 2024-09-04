from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# 1) MAİN / VIEWS.PY     faylında yaradılan index() və about() metodları sadəcə İNDEX.HTML və ABOUT.HTML şablonlarını RENDER edir. Burada DB-ə edilen hər hansısa bir sorğu yoxdur onun üçündə
#    yəni sadə olduğu üçündə  `TemplateView`   class-ından istifadə edəcəyik. 

# 2) İlk öncə öz class-ımızı yaratmalıyıq və bu class-a deməliyik ki, TemplateView class-ını izlə. Bu class-ın işləmə prinsipi dokumentasiyada yazılıbdır. Öz class-ımızın adı olsun `İndexView`
#    RENDER avtomatik olaraq baş verir və REQUEST və.s göndərməyə ehtiyac yoxdur. 
class IndexView(TemplateView):
    # 3) Şablon faylının adını     `template_name`      variable-ılı içinə yazırıq. 
    template_name = 'main/index.html'

    # 4) Şablona CONTEXT göndərmək üçün isə    `GET_CONTEXT_DATA`    funksiyasından istifadə edirik. Bu funksiyanin adı mütləq bu cür yazılmalıdır əks halda şablona data göndərmək olmayacaqıdr.
    # 5) **kwargs - Keyword Arguments     deməkdir və DİCT yaradaraq     `açar söz il => dəyər`     əldə etmək üçün istifadə edilir. Bu data-lar isə, əgər lazım olarsa şablonda istifadə edilməsi üçün 
    #    default olaraq DJANGO tərəfindən   `kwargs`   parametrinə verilən context datalarıdır. 
    def get_context_data(self, **kwargs):
        # 6) SUPER()  funksiyası       TemplateView      class-ına müracietə etmək üçün istifadə edilir.  Sonra isə həmin class-ın içində olan orgianl     get_context_data()   metodunu əldə edirik. 
        #    Bu metotdan DJANGONUN bəzi default olaraq ehtiva etdiyi data-ları şablona göndərmək üçün istifadə edilir. Kodu belə də yazsaq işləyəckdi:
                                                                                                                                                        # def get_context_data(self):
                                                                                                                                                        #     context = {}
                                                                                                                                                        #     context['title'] = 'Home - Main page'
                                                                                                                                                        #     context['content'] = 'Magazine of furniture'
                                                                                                                                                        #     return context
        # Ancaq doğru olamaycaqdır. Çünki Django da olan default context datalarından istifadə edə bilməyəcəyik. Məsələn URL parametrləri. 
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Main page'
        context['content'] = 'Magazine of furniture'
        return context
    # 7) class-ları yaratdıqdan sonra isə,      MAİN / URLS.PY     faylında marşrut yolunu bu cür yazmaq lazımdır:                  path('', views.IndexView.as_view(), name='index')
 




# 8) Eyni proseduru About ucunde edirik. 
class AboutView(TemplateView):
    template_name = 'main/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - about page'
        context['content'] = 'Here is some text about us'
        context['text_on_page'] = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text '
        return context