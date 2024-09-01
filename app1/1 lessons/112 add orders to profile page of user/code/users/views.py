from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from carts.models import Cart
from orders.models import Order, OrderItem


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, You are now logged in")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
        
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('users:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title' : ' Home - Authorization ',
        'form' : form
    }
    return render( request, 'users/login.html', context )



def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            
            messages.success(request, f"{user.username}, You are now registered and logged in")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {
        'title' : ' Home - Authentication ',
        'form' : form,
    }
    return render( request, 'users/registration.html', context )





@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            messages.success(request, "Profile successfully updated")
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    # 1) Istifadəçinin PROFİLE səhifəsində onun etdiyi ORDER-ləri göstərmək üçün aşağıdakı kimi yazırıq. Aşağıdakı kod, istifadəçinin sifarişlərini (ORDER modelindən) və hər bir sifarişlə əlaqəli məhsul məlumatını (Orderİtem modelindən) 
    #    səmərəli şəkildə sorğulamaq üçün yazılmışdır.
    orders = (
        # 2) ORDER modelindən istifadəçiyə görə onun sifarişlərini FİLTER metodu ilə əldə edirik. (user_id, phone_number, delivery_address və.s)
        #    * PREFETCH_RELATED() - fetch ingilis dilində gətirmək deməkdir. PRE ön şəkilçisi ilə əvvəlcədən mənasına gəlir. Related sözü artıq mövcud olan qohumluq əlaqəsi mənasına gəlir (keçmiş zaman). Sözün tamam isə bu mənaya gəlir:
        #    Qurulmuş qohumluq əlaqəsinə əsasən əvvəlcədən əldə etmək. Yəni, bu metod Django ORM-dən, bir-birilə əlaqəli olan modelləri DB-dən, əldə etmək üçün istifadə edilir. Bu qayda əlaqə model məlumatlarını ayrı bir sorğu ilə 
        #    əvvəlcədən yükləyərək performansı artırır. 
        #    * PREFETCH() klası ilə, PREFETCH_RELATED() içindəki sorğuları xüsusiləşdirmək üçün istifadə edilir. PREFETCH_RELATED() metodu, əlaqəli modelləri əldə edərkən onları yaddaşda saxlıyar. Bu metodu xüsusiləşdirmək istədikdə
        #      Yəni əlaqəli modeldən gələn məlumatları, xüsusi bir şərtə görə filtirləmək, sıralamaq yaxud sadəcə xüsusi sahələri əldə etmək istədikdə PREFECTH klasından istifadə edilir. 
        #    * Bu klasın 1ci parametri:   Order modelinə bağlı OrderItem'ları almağı ifade edir. Nə üçün ORDERİTEM_SET yazılır ? Bu parametr dediyimiz kimi Order modelinə bağlı Orderİtem-ları almaq üçün lazımdır. Bu parametri yazmağımızın
        #      səbəbi isə MODEL-i yaratdığımız da RELATED_NAME -dən istifadə etməmiş olmağımızdır:    
        #                                                                                           class OrderItem(models.Model):
        #                                                                                               order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
        #      
        #      Əgər bu cür yazmış olsaydıq Order-ə bağlı OrderItem'ları əldə etmək üçün bu parametr içindəki İTEMS dəyərindən istifadə edə bilərdik:            order_items = order.items.all()
        #      
        #      Ancaq, əvvəlcədən RELATED_NAME yazmamışıq deyə, PREFETCH() klasında bu əlaqə _SET şəkilçisinə Orderİtem model adına qoşaraq yaradırıq. ORDERİTEM_SET, django'nun default olarak yaratdığı əlaqə adıdır. Order modeline bağlı bütün
        #      OrderItem datalarını əldə etmək üçün istifadə edilir. Bu default adı dəyişdirmək istəsək, ForeignKey sahəsində RELATED_NAME parametrini yazacağıq. Bu sayədə, bir modelin əlaqədə olduğu diğər modelin datalarını əldə edə bilərik.
        #       
        #      * Bu klasın 2ci parametri ilə göndərilən sorğu, `Orderİtem` modelindəki dataları alarkən, hər Orderİtem-a bağlı olan PRODUCT məlumatlarınıda SELECT_RELATED istifadə edərək alır. Bu əlaqə PRODUCT modelinin datalarını tək sorğu
        #        ilə əldə etməyə imkan yaradır. 
        #        
        #      * ORDER_BY('-İD')  - bu hissə isə, sorğu nəticələrini İD sahəsinə görə azalan -İD sıra ilə sıralamaq üçün istifadə edilir.    Bu isə, ən son sifarişin ilk sırada olması üçündür. 
        #      
        #      * Təbii ki, daha sadə yazardıq yəni belə: 
        #                                                orderİd = Order.objects.filter(user=request.user)
        #                                                orderitem=OrderItem.objects.filter(order=orderİd)            Ancaq   `PREFETCH_RELATED`  və  `SELECT_RELATED`   kimi qaydalar, sorğu sayısını azaldaraq performansı optimize edir. 
        #       
        #        Sadə sorğuda, Orderİtem-ı  əldə edərkən,  hər bir  Orderİtem  üçün bir sorğu yaradılır və N+1 problemi yaranır. Yəni, 10 sifariş varsa, hər biri üçün Orderİtem sorğulanır və 11 sorğu yaradılmış olur. Biraz qarmaşıq olan
        #        qaydada isə, ORDER modelinə bütün ORDERİTEM obyektləri, xüsusi sorğu ilə (məsələn PRODUCT ilə əlaqəli datalarıda daxil edilərək) əvvəlcədən gətirilir.  SELECT_RELATED('PRODUCT') ilə də,  ORDERİTEM obyektinin hər biri ilə
        #        bağlantılı olan PRODUCT məlumatları TƏK SORĞUDA əldə edilmiş olur. 
        #
        #       * SELECT_RELATED   - bu qayda,  "ForeignKey"      vəya  "OneToOneField"       əlaqəsi olan modellərdə istifadə edilir. Əlaqəli modeli tək  SQL sorğusu ilə gətirir və hər obyekt üçün ayrı sorğu yaradılmır. 
        #       * PREFETCH_RELATED - bu qayda,  "ManyToManyField" vəya  "reverse ForeignKey"  əlaqəsi olan modellərdə istifadə edilir. Əlaqəli modeli ayrı SQL sorğusu ilə gətirir və Python tərəfində birləşdirir. SELECT_RELATED-dən
        #         fərqli olaraq, PREFETCH_RELATED clası eyni vaxtda birdən çox sorğunu işlədə bacarır və eyni vaxtda birdən çox obyekt ilə əlaqəli dataları gətirmək üçün istifadə edilir. 
        Order.objects.filter(user=request.user)
            .prefetch_related( 
                Prefetch( 
                        "orderitem_set", 
                        queryset=OrderItem.objects.select_related('product'), 
                ) 
            ).order_by('-id')
    )

    context = {
        'title' : ' Home - Profile ',
        'form' : form,
        # 3) TUPLE tipində ORDERS adında variable yaradaraq bura sifarişləri qoyduq həmin variable-a və CONTEXT ilə şablona göndərdik. 
        'orders' : orders
    }
    return render( request, 'users/profile.html', context )
@login_required



def users_cart(request):
    return render(request, 'users/users_cart.html')


def logout(request):
    messages.success(request, f"{request.user.username}, You are now logged out")
    auth.logout(request)
    return redirect(reverse('main:index'))




