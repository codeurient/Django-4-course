from django import forms



class CreateOrderForm(forms.Form):
    
   
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    # 1) ChoiceField() class-ı üçün   choices   parametrini əlavə etmək lazımdır. 
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", "False"),
            ("1", "True"),
        ],
    )
    delivery_address = forms.CharField(required=False)
    # 2) ChoiceField() class-ı üçün   choices   parametrini əlavə etmək lazımdır. 
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", "False"),
            ("1", "True"),
        ],
    )






