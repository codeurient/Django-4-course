from ast import pattern
from django import forms
import re


# 1) Digər dərslərdə model ilə əlaqəli olan form-ları yaratdıqda, bu form-lar xüsusi validator -lar ilə işləyirdi. Ancaq biz öz xüsusi validatorlarımızı yara bilərik. 
#    Bu validatorlar da input sahələrinə yazılan dəyərlərin doğruluğunu yoxlaya bilər. 
class CreateOrderForm(forms.Form):
    
   
    first_name = forms.CharField()

    last_name = forms.CharField()

    phone_number = forms.CharField()

    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", "False"),
            ("1", "True"),
        ],
    )

    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", "False"),
            ("1", "True"),
        ],
    )

    # 2) Sahələr üçün öz əlavə validatorlarımızı yaratdıqda CLEAN deyilən ön şəkilçidən istifadə edilir. DJANGO avtomatik başa düşür ki, hansı sahə üçün əlavə validasiya yaratmaq lazımdır.
    def clean_phone_number(self):
        # 3) INPUT sahesine girilən dəyəri əldə edirik
        data = self.cleaned_data['phone_number']

        # 4) Əgər girilən dəyər ədəd deyilsə aşağıdakı mesajı göstəririk. 
        if not data.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")

        # 5) Qaydalı ifadə yaradaraq başqa bir şərt daha qoşaraq deyirik ki, girilən dəyər 10 dan çox ola bilməz 
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError("Phone number must be 10 digits long.")
        
        # 6) Əgər hər şey doğru girilərsə onda həmin dəyəri RETURN edirik. 
        return data
    

    