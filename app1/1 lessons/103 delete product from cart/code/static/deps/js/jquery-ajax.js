$(document).ready(function () {
    // 1) ajax bildirişləri üçün    NOTİFİCATIONS.HTML  faylındakı ID-si   'jq-notification'   olan    DİV elementini variable-a yerləsdiririk
    var successMessage = $("#jq-notification");

    // 2) Class deyeri   'add-to-cart'    olan A tag-inə CLİCK event-ını veririk. Bu A tag-i məhsulu səbətə əlavə etmək üçün istifadə etdiyimiz səbət ikonudur. Həmin səbət ikonu klikləndikdə Funksiya işləyəcək.
    $(document).on("click", ".add-to-cart", function (e) {
        // 3) A tag-inin default xüsusiyyətlərini blokluyuruq. 
        e.preventDefault();

        // 4) Sol tərəfdəki Səbət ikonundakı sayğac elementinin dəyərini götürmək üçün SPAN tag-ini çağırırıq 
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0); // SPAN tag-inin içindəki dəyəri əldə edirik

        // 5) A tag-inə    DATA-PRODUCT-İD    adında atribut əlavə edərək bu atrbibuta məhsulun İD-sini veririk və aşağıdakı script ilə həmin A tag-inin bu atributunun dəyərini yəni məhsulun ID-sini alırıq. 
        var product_id = $(this).data("product-id");

        // 6) A tag-inin href atributundakı linkin dəyərini alırıq. Bu link hansıki bizi controller-ə yönləndirən linkdir.
        var add_to_cart_url = $(this).attr("href");

        // 7) Səhifəni yeniləmədən AJAX sorğu göndəririk.
        $.ajax({
            type: "POST",           // 8) POST metodundan istifadə edirik
            url: add_to_cart_url,   // 9) Controller-ə yəni   'cart_add/'    url-sinə aşağıdakı data-nı göndəririrk. 
            data: {                 // 10) Bu data-nı göndərirrik. 
                product_id: product_id, // 11) Göndərilən data məhsulun identifikatorudur. Bu İD-nı A tag-inin    'data-product-id={{ product.id }}'   atributundan əldə edirik. AJAX sorğunun POST metodu ilə göndərilən PRODUCT_İD-ni  
                                        //     CARTS / VIEWS.PY   controllerində,  REQUEST parametri ilə əldə edirik.           
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),     // 12) CSRF token-idə göndəririk. A tag-inin içinə əlavə edilən CSRF tokeni bu script avtomatik olaraq əldə edir. 
            },
            success: function (data) { // 13) JS bizdən geri cavab gözlüyəcək. Həmin cavab JSON formatında bu funksiyanın DATA parametrinə gələcək. 
                // 14) NOTİFİCATIONS.HTML faylındakı DİV tag-inə məlumat əlavə edilir.
                successMessage.html(data.message); 
                successMessage.fadeIn(400);
                // 15) 7 saniye sonra hemin xəbərdarlıq mesajını gizlədirik. 
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                // 16) Sol tərəfdəki səbət ikonunda ola məhsul miqdarını artırıqı. 
                cartCount++;
                goodsInCartCount.text(cartCount);  // 17) Artan sayı, SPAN tag-inin içinə yerləşdiririk.
                // 18) TEMPLATES / INCLUDES / CART_BUTTON.HTML,     USERS / TEMPLATES / USERS / PROFILE.HTML  və  USERS / TEMPLATES / USERS / USERS_CART.HTML     faylındakı DİV tag-ini çağırırıq. 
                var cartItemsContainer = $("#cart-items-container"); 
                // 19) Controller-dən gələn JSON formatındakı məlumatları HTML metodu ilə çevirərək DİV tag-inə əlavə edirik.
                cartItemsContainer.html(data.cart_items_html);
            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });




    // Bir məhsulu səbətdən silmək üçün       İNCLUDED_CART.HTML       faylından A tag-ini çağırırıq və ona EVENT veririk. 
    $(document).on("click", ".remove-from-cart", function (e) {
        e.preventDefault();

        // CART_BUTTON.HTML  faylından SPAN tag-ini əldə edirik. Bu span tag-inin içində məhsulun miqdarı vardır. 
        var goodsInCartCount = $("#goods-in-cart-count");
        var cartCount = parseInt(goodsInCartCount.text() || 0);   // SPAN tag-inin içindəki məhsulun sayını alırıq.

        // A tag-inə  DATA-CART-İD    deyə bir atribut əlavə etmişik. Bu atributun içində isə dəyər olaraq səbətin İD-si mövcuddur. Bu atributun dəyəri əldə ediləcək.
        var cart_id = $(this).data("cart-id");
        // A tag-inin HREF atributunun icindeki deyeri gotururuk. Bu deyer bizi Controller-ə götürən linkdir. 
        var remove_from_cart = $(this).attr("href");
    
        // AJAX sorğu göndəririk. 
        $.ajax({
            type: "POST",
            url: remove_from_cart, // Controller-ə 
            data: {                 // DATA göndərilir.
                cart_id: cart_id,   // Gonderilen data səbətdəki məhsulun İD-sidir. 
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                successMessage.html(data.message); // Məhsul silindikdən sonra göstəriləcək mesaj
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                // Məhsul silindikdən sonra    CART_BUTTON.HTML  faylındakı  SPAN tag-inin içindən sayı azaldırıq.  QUANTİTY_DELETED  bizə CARTS / VIEWS.PY controllerinden gəlir. 
                cartCount -= data.quantity_deleted;
                goodsInCartCount.text(cartCount); // Say azaldıqdan sonra text() metodu ilə təkrar SPAN tag-inə yeni sayı əlavə edirik.

                // TEMPLATES / INCLUDES / CART_BUTTON.HTML,     USERS / TEMPLATES / USERS / PROFILE.HTML  və  USERS / TEMPLATES / USERS / USERS_CART.HTML     faylındakı DİV tag-ini çağırırıq. 
                var cartItemsContainer = $("#cart-items-container");
                // Controller-dən gələn JSON formatındakı məlumatları HTML metodu ilə çevirərək DİV tag-inə əlavə edirik.
                cartItemsContainer.html(data.cart_items_html);
            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });




    // // Теперь + - количества товара 
    // // Обработчик события для уменьшения значения
    // $(document).on("click", ".decrement", function () {
    //     // Берем ссылку на контроллер django из атрибута data-cart-change-url
    //     var url = $(this).data("cart-change-url");
    //     // Берем id корзины из атрибута data-cart-id
    //     var cartID = $(this).data("cart-id");
    //     // Ищем ближайшеий input с количеством 
    //     var $input = $(this).closest('.input-group').find('.number');
    //     // Берем значение количества товара
    //     var currentValue = parseInt($input.val());
    //     // Если количества больше одного, то только тогда делаем -1
    //     if (currentValue > 1) {
    //         $input.val(currentValue - 1);
    //         // Запускаем функцию определенную ниже
    //         // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
    //         updateCart(cartID, currentValue - 1, -1, url);
    //     }
    // });

    // // Обработчик события для увеличения значения
    // $(document).on("click", ".increment", function () {
    //     // Берем ссылку на контроллер django из атрибута data-cart-change-url
    //     var url = $(this).data("cart-change-url");
    //     // Берем id корзины из атрибута data-cart-id
    //     var cartID = $(this).data("cart-id");
    //     // Ищем ближайшеий input с количеством 
    //     var $input = $(this).closest('.input-group').find('.number');
    //     // Берем значение количества товара
    //     var currentValue = parseInt($input.val());

    //     $input.val(currentValue + 1);

    //     // Запускаем функцию определенную ниже
    //     // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
    //     updateCart(cartID, currentValue + 1, 1, url);
    // });

    // function updateCart(cartID, quantity, change, url) {
    //     $.ajax({
    //         type: "POST",
    //         url: url,
    //         data: {
    //             cart_id: cartID,
    //             quantity: quantity,
    //             csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
    //         },
 
    //         success: function (data) {
    //              // Сообщение
    //             successMessage.html(data.message);
    //             successMessage.fadeIn(400);
    //              // Через 7сек убираем сообщение
    //             setTimeout(function () {
    //                  successMessage.fadeOut(400);
    //             }, 7000);
 
    //             // Изменяем количество товаров в корзине
    //             var goodsInCartCount = $("#goods-in-cart-count");
    //             var cartCount = parseInt(goodsInCartCount.text() || 0);
    //             cartCount += change;
    //             goodsInCartCount.text(cartCount);

    //             // Меняем содержимое корзины
    //             var cartItemsContainer = $("#cart-items-container");
    //             cartItemsContainer.html(data.cart_items_html);

    //         },
    //         error: function (data) {
    //             console.log("Ошибка при добавлении товара в корзину");
    //         },
    //     });
    // }










    //! 1)  JQUERY-EVENTS.JS   faylindan goturduyumuz kodlari yerlesdiririk bura. 





    var notification = $('#notification');
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }   


    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    $("input[name='requires_delivery']").change(function() {
        var selectedValue = $(this).val();
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });
});