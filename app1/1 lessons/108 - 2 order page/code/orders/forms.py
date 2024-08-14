from django import forms



class CreateOrderForm(forms.Form):
    
    # 2) İndi gedirik       ORDERS / TEMPLATES / ORDERS / CREATE_ORDER.HTML      faylına.
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField()
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField()



















# 1) Öz class form-umuzu yaradırıq. Buarada USER-da olduğu kimi META class-ı yoxdur. Burada manual olaraq yazmışıq ki hansı sahələr üçün FORMS istifadə ediləcək. Bu sahə adlarıda 
#    model-imizdə olan adlar ilə eynidir. Bu qayda ilə FRONT-in bir hissəsini BACKEND-də yazmış olduq. Hansı ki, bu qayda məsləhət deyildir. Sadəcə praktika olsun deyə indi yazdıq.
#    Bu kodlari comment-e aliriq və yuxarıda sadə qayda ilə yenidən yazırıq.  
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control', 
    #             'placeholder': 'Enter your name'
    #         }
    #     )
    # )

    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control', 
    #             'placeholder': 'Enter your lastname'
    #         }
    #     )
    # )

    # phone_number = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control', 
    #             'placeholder': 'Enter your phone number'
    #         }
    #     )
    # )

    # requires_delivery = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #     ],
    #     initial=0,
    # )

    # delivery_address = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'form-control', 
    #             'id': 'delivery-address',
    #             'rows': 2, 
    #             'placeholder': 'Enter delivery adress'
    #             }
    #         ),
    #     required=False,
    # )

    # payment_on_get = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #     ],
    #     initial="card",
    # )   


