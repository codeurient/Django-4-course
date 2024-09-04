from django.contrib.auth.decorators import login_required
# 1) 
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm
from carts.models import Cart
from orders.models import Order, OrderItem





# 2) UserLoginView adında class yaradırıq və  LoginView clas-ını izləməsini deyirik. 
class UserLoginView(LoginView):
    template_name = 'users/login.html'
    # 3) Burda digər məsələn product da olduğu kimi model adını yazmıyıq.  Forms.py faylında olan     UserLoginForm  class-ının adını yazırıq. Çünki həmin class birbaşa model ilə əlaqəlidir.   form_class  proqram variable-ıdır.  
    form_class = UserLoginForm
    # 4) success_url   variable-ı ilə əgər istifadəçi uğurla giriş etdisə onu hara yönləndirmək lazım olduğunu deyirik.             success_url  proqram variable-ıdır.  
    success_url = reverse_lazy('main:index')




    # Bu hissəni artıq görmüşük bilirik. 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Authorization'
        return context

























# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             session_key = request.session.session_key

#             if user:
#                 auth.login(request, user)
#                 messages.success(request, f"{username}, You are now logged in")

#                 if session_key:
#                     forgot_carts = Cart.objects.filter(user=user)
#                     if forgot_carts.exists():
#                         forgot_carts.delete()

#                     Cart.objects.filter(session_key=session_key).update(user=user)
        
#                 redirect_page = request.POST.get('next', None)
#                 if redirect_page and redirect_page != reverse('users:logout'):
#                     return HttpResponseRedirect(request.POST.get('next'))
#                 return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserLoginForm()
#     context = {
#         'title' : ' Home - Authorization ',
#         'form' : form
#     }
#     return render( request, 'users/login.html', context )






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



