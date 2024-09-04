from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from carts.models import Cart
from orders.models import Order, OrderItem


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('user:logout'):
            return redirect_page
        return reverse_lazy('main:index')
    

    # 1) Istifadəçi qeydiyyatdan keçmədən əvvəl səbətə əlavə edən məhsulları, qeydiyyatdan keçdikdən sonra onun səbətinə əlavə etmək üçün ilk öncə FORM_VALİD adında funksiya yaradırıq. Çünki bu metod o vaxt işləycək ki, 
    #    proqram yoxlasın ki, sistemdə istifadəçi mövcuddurmu. Yəni istifadəçinin validliyini kontrol edir və varsa əgər istifadəçi ondan sonra həmin funksiyanın içindəki kodlar işləyir. NOT LOGİN olmaqla REGİSTRATİON olmağı 
    #    səhf salmayaq. Əgər istifadəçi REG olubdursa ancaq LOGİN olmayıbdırsa bu funksiya yenədə işləyəcək.
    def form_valid(self, form):
        # 2) LOGİN olmadan səbətə məhsul əlavə etmək istədikdə SESSİON_KEY variable-ına sessiya açarını yerləşdiririk. 
        session_key = self.request.session.session_key

        # 3) Sonra USER-ı əldə edirik. 
        user = form.get_user()

        # 4) Əgər belə bir istifadəçi varsa
        if user:
        # 5) Onu LOGİN edirik. Django avtomatik olaraq bu istifadəçi üçün yeni SESSİON_KEY yaradır. 
            auth.login(self.request, user)

            # 6) Əgər yeni SESSİON KEY varsa köhnə dataları CART içindən silirik və SESSİON ilə əlavə edilənlə CART modelini UPDATE edirik. 
            if session_key:
                forgot_carts = Cart.objects.filter(user=user)
                if forgot_carts.exists():
                    forgot_carts.delete()
                Cart.objects.filter(session_key=session_key).update(user=user)
                # 7) Hər şey uğurlu oldusa      `You are logged in to your account`    deyə mesaj göstəririk.
                messages.success(self.request, f"{user.username}, You are logged in to your account")

                return HttpResponseRedirect(self.get_success_url())


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Authorization'
        return context















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

    orders = (
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




