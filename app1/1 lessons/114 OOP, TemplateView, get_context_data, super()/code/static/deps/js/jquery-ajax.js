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
                console.log("Error adding product to cart");
            },
        });
    });




    //  +  Ve -  
    // INCLUDED_CART.HTML   faylindaki BUTTON tag-ini elde edirik.
    $(document).on("click", ".decrement", function () {
        // BUTTON tag-inin CART-CHANGE-URL atributunun deyerini elde edirik:        {% url "cart:cart_change" %}
        var url = $(this).data("cart-change-url");
        //  BUTTON tag-inin CART-ID atributunun deyerini elde edirik:               CART.ID  - sebete elave edilen her hansisa bir mehsulun identifikatorudur. 
        var cartID = $(this).data("cart-id");
       
        // DIV tag-inin icindeki INPUT tag-ini obyekt icinde elde edirik:         ce.fn.init {0: input.form-control.number, length: 1, prevObject: ce.fn.init}
        var $input = $(this).closest('.input-group').find('.number');
        // Hemin INPUT tag-inin icinde olan deyeri elde edirik: Meselen, 5, yaxud 3, yaxud 1 ve.s
        var currentValue = parseInt($input.val());
        // Eger bu INPUT tag-inin icindeki deyer 1 den cox olarsa onda hemin movcud deyerden 1 cixiriq eks halda hecne etmirik. 
        if (currentValue > 1) {
            $input.val(currentValue - 1);
            // Decremet BUTTON-u her defe kliklendikde eger IF true vererse onda asagidaki UPDATECART() funksiyasi cagrilir ve morterize icindeki arqumentler gonderilir. Bu metod vasitesi ile DB-si yenileyeceyik.
            updateCart(cartID, currentValue - 1, -1, url); 
        }
    });

    // Eyni prosedurani INCREMENT ucunde edirik. 
    $(document).on("click", ".increment", function () {
        var url = $(this).data("cart-change-url");
        var cartID = $(this).data("cart-id");
        var $input = $(this).closest('.input-group').find('.number');
        var currentValue = parseInt($input.val());
        $input.val(currentValue + 1);
        updateCart(cartID, currentValue + 1, 1, url);  // INCREMENT olanda +1 gonderirik.
    });

    // DECREMENT ve INCREMENT prosedurlarindan sonra,  updateCart() funksiyasini cagiririq.
    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
 
            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                     successMessage.fadeOut(400);
                }, 7000);
 
                // TEMPLATES / INCLUDES / CART_BUTTON.HTML     faylındakı sebet ikonunu emele getiren SPAN tag-ini çağırırıq. 
                var goodsInCartCount = $("#goods-in-cart-count");
                var cartCount = parseInt(goodsInCartCount.text() || 0);  // SPAN tag-inin icindeki sayı elde edirik.
                cartCount += change;            // Həmin sayı 1 artırıq yaxud 1 azaldırıq. 
                goodsInCartCount.text(cartCount);  // Sonra SPAN tag-ine artmış olan yaxud azalmış olan sayı yerləşdiririk. 

                // TEMPLATES / INCLUDES / CART_BUTTON.HTML,     USERS / TEMPLATES / USERS / PROFILE.HTML  və  USERS / TEMPLATES / USERS / USERS_CART.HTML     faylındakı DİV tag-ini çağırırıq. 
                var cartItemsContainer = $("#cart-items-container");
                // Controller-dən gələn JSON formatındakı məlumatları HTML metodu ilə çevirərək DİV tag-inə əlavə edirik.
                cartItemsContainer.html(data.cart_items_html);

            },
            error: function (data) {
                console.log("Error adding product to cart");
            },
        });
    }










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






        document.getElementById('id_phone_number').addEventListener('input', function (e) {
            var x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
            e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
        });
    
        $('#create_order_form').on('submit', function (event) {
            var phoneNumber = $('#id_phone_number').val();
            var regex = /^\(\d{3}\) \d{3}-\d{4}$/;
    
            if (!regex.test(phoneNumber)) {
                $('#phone_number_error').show();
                event.preventDefault();
            } else {
                $('#phone_number_error').hide();
    
                // Очистка номера телефона от скобок и тире перед отправкой формы
                var cleanedPhoneNumber = phoneNumber.replace(/[()\-\s]/g, '');
                $('#id_phone_number').val(cleanedPhoneNumber);
            }
        });



});