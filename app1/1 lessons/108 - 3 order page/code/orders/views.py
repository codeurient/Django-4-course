from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from carts.models import Cart

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem




def create_order(request):
    if request.method == 'POST':
        # 1) POST metodi ilə şablondan göndərilən data-ları ötürürük     CreateOrderForm( )    class-ına. Bu Class şablon elementlərimizin valdasiyasını kontrol edəcək. 
        form = CreateOrderForm(data=request.POST)

        # 2) Bu İF ilə hələki işimiz yoxdur. Bu İF, biz, şablonda olan tag-ləri düzgün doldurduqda İS_VALİD() metodu həmin tag-ləri yoxladıqdan sonra TRUE qaytardıqda işləyəcək. 
        if form.is_valid():
            try:
                # 4) 'WITH'   konstruktorundan və   'TRANSACTION.ATOMIC()' -dən   istifadə edilməsi verilənlər bazası əməliyyatlarının atomik əməliyyat kimi həyata keçirilməsini təmin edir. Bu əməliyyatların, hamısının uğurla başa 
                #     çatmasını yaxud xəta olarsa geri qaytarılmasını (rollback) təmin edir.
                #     Bir kod 'WITH' blokuna daxil olduqda açılır və blokdan çıxdıqda avtomatik qapanır. Məsələn sənədlərin oxunması, yazılması və.s. Beləliklə 'WITH' ifadəsi kodların güvənli formada idarə edilməsini təmin edir.
                #     'TRANSACTION.ATOMIC()' ifadəsi, Django-da DB əməliyyatlarını ATOMİK blok içində işləyir. Yəni kodda yazdığımız hər şey düz olarsa edilən əməliyyatlar DB-sə göndərilir əks halda EXCEPTİON baş verən xətanı 
                #     tutaraq bizə göstərir. Bu qayda DB-in bütünlüyünün qorunmasını qaranti edir.  Bizim yazdığımız kodda məsələn istifadəçi hər hansısa bir məhsul sifariş etdikdə xəta baş verərsə ( Məsələn stokda kifayət qədər 
                #     məhsul yoxdursa. ) onda bütün əməliyyatlar geri alınır və məhsul sifarişi yarıda qalmamış olur. 
                #     Deyək ki, istifadəçi bir neçə məhsul sifariş edir və bir məhsul stokda yoxdur. Bu halda,  'TRANSACTION.ATOMIC()'  sayəsində bütün sifariş ləğv edilir və verilənlər bazasında heç nə saxlanmır.
                with transaction.atomic():
                    #5) İstifadəçi SUBMİT düyməsini kliklədikdə, bu düyməni basan istifadəçini REQUEST.USER yazaraq əldə edirik. 
                    user = request.user
                    # 6) Sonra CART modelində yəni SƏBƏT cədvəlində olan USER sütunundakı istifadəçi ilə düyməni klikləyən istifadəçini eyniləşdirərək həmin istifadəçinin səbətindəki məhsulları əldə edirik. 
                    cart_items = Cart.objects.filter(user=user)
                    # 7) Burada deyirik ki, eger sebetde mehsul varsa
                    if cart_items.exists():    
                        # 8) CREATE() adlı metodla ORDER modelini yaratırıq və bu modeli `order` variable-ına veririk. 
                        order = Order.objects.create(
                            user=user,                                                      # 9) Order modelinin User sütununa istifadəçi İD-sini qoyuruq ki,səbətdəki məhsulu hansı istifadəçi sifariş edir bilək. 
                            phone_number=form.cleaned_data['phone_number'],                 # 10) Yuxarıdaki FORM vairable-ından POST metodu ilə əldə etdiyimiz dəyərləri götürürük. 
                            requires_delivery=form.cleaned_data['requires_delivery'],       # 11) Radio tipi ilə seçilən 1 yaxud 0 dəyərlərindən birisini əldə edirik.    
                            delivery_address=form.cleaned_data['delivery_address'],         # 12) Textarea tag-inə daxil edilən adresi dəyərini əldə edirik.
                            payment_on_get=form.cleaned_data['payment_on_get'],             # 13) Radio tipi ilə seçilən 1 yaxud 0 dəyərlərindən birisini əldə edirik.  
                        ) # 14) CLEANED_DATA, Django-da forma məlumatlarını daha təmiz formada əldə etməyə imkan yaradan DİCT strukturudur.
                       
                        # 15) Bu FOR döngüsü növbəti Orderİtem cədvəli üçündür. For döngüsü ilə, CART_İTEMS da olan bütün məhsulları əldə edərək CART_İTEM variable-ına ötürür. 
                        for cart_item in cart_items: 
                            product=cart_item.product           # 16) Səbətdəki hər Product-un özünü əldə edirik. Bu Product sözü Cart modelindeki ForeignKey Product sütununun adıdır. Və bu sütunda Product identifikatorları var. 
                            name=cart_item.product.name              # 17) Cart modelində ki, ForeignKey olan Product sütunu vasitəsi ilə Product modlinin Name sütununa müraciət edərək məhsulun adını əldə edirik. 
                            price=cart_item.product.sell_price()     # 18) Eyni qayda ilə məhsulun qiymətini əldə edirik. 
                            quantity=cart_item.quantity              # 19) Səbətə əlavə edilən hər məhsulun miqdarını əldə edirik. 

                            # 20) Product modelindəki məhsulun miqdarı, Sifariş edilmək üçün Səbətə əlavə edilən məhsulun miqdarından az olarasa TRUE qayıdacaq və İF işləyərək bizə `Not enought product` mesajını göstərəck. 
                            if product.quantity < quantity:
                                raise ValidationError(f'Not enough product {name} in stock \ In stock - {product.quantity}')
                            
                            # 21) Əks halda OF olacaq FALSE və aşağıdakı kod işləyəck. Orderİtem modelində Create() metodu ilə Sifariş (sifariş edilən məhsul əlavə ediləcək) yaradılacaq. 
                            OrderItem.objects.create(
                                order=order,            # 22) Orderİtem modelinin Order     sütununa Order    modelinin ID-sini qoyuruq.
                                product=product,        # 24) Orderİtem modelinin Product   sütununa Cart     modelindəki Product sütununda olan hər məhsulun ID-sini ayrı-ayrə əldə edərək qoyuruq. FOR döngüsü sayəsində. 
                                name=name,              # 25) Orderİtem modelinin Name      sütununa Product  modelindəki Name sütununda olan məhsulun adını əlavə edirik. 
                                price=price,            # 26) Orderİtem modelinin Price     sütununa Product  modelindəki sell_price() metodu ilə əldə edilən məhsulun qiymətini əlavə edirik.
                                quantity=quantity,      # 27) Orderİtem modelinin Quantity  sütununa Cart     modelindəki Quantity sütununda olan məhsulun miqdarını əlavə edirik.
                            )
                            # 28) Product modelinin Quantity sütununda olan hər məhsulun miqdarından Səbətə (cart) əlavə edilən hər məhsulun miqdarını çıxırıq. Fərqli məhsullardan fərqli miqdar çıxılır çünki For döngüsü ilə səbətdə olan 
                            #     birdən çox məhsulu ayrı-ayrı əldə etmişik. 
                            product.quantity -= quantity
                            # 29) Sonra SAVE() meotdu ilə bu Product modelindəki dəyişikliyi yadda saxlayırıq. 
                            product.save()
                        # 30) Sifariş yaradıldıqdan sonra CART modelinin içini təmizləyirik. 
                        cart_items.delete()
                        # 31) Sonra sifariş tamamlandı deyə mesaj göstəririk. 
                        messages.success(request, 'Order completed!')
                        return redirect('user:profile') # 32) Və İstifadəçini Profile səhifəsinə yönləndiririk. 
            # 33) Əgər kodda xəta olarsa onda mesaj olaraq bu xətanı göstərəcəyik və istifadəçini   http://127.0.0.1:8000/orders/create_order    səhifəsinə yönləndirəcəyik.   
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('orders:create_order')
    
    # 3) Bu ELSE isə POST sorğu yoxdursa işləyəcək. Buda GET sorğudur.    
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            }
        # 4)  İNİTİAL     parametri ilkin məlumatlar mənasına gəlir. Bu parametr yuxarıda yaratdığımız DİCT-i qəbul edir. Bu məlumatlar SUBMİT düyməsi kliklənmədən biz sayta giriş edən zaman USER model-indən əldə edilir.
        #     və CreateOrderForm() klasının INITIAL parametri ilə default dəyər olaraq işə salınır. İnitial sözünün mənasıda işə salmaq, başlatmaq mənasına gəlir. Şablonda isə dəyərləri əldə etmək üçün belə yazırıq:
        #      
        #     form.first_name.value
        #     
        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Home - Placing an order',
        'form': form,
    }
    return render(request, 'orders/create_order.html', context=context)








