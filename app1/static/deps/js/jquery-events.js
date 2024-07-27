// 1) Burda JS-in Jquery adlı kitabxanasından istifadə etmişik. 
$(document).ready(function () {
    // 2) Elementi İD-si ilə əldə edirik. Bu Django nun xəbərdarlıq mesajını göstərən pəncərədir. Həmin elementi konsola yazdırdıqda görərik ki onun LENGTH
    //    adında bir parametri var və dəyəri birdir. 
    var notification = $('#notification');
    // 3) Buna görə də NOTİFİCATİON.LENGTH ilə 1-i əldə edərək 0 (sıfır)-la müqayisə edirik və nəticə TRUE olacağı üçün İF işləyəcək.
    if (notification.length > 0) {
        // 4) 7 saniyə sonra isə pəncərəni qapadırıq.
        setTimeout(function () {
            // 5) Pencereni qapatmaq ucun ise Bootstrap-in ALERT('close') metodundan istifadə edirik.
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