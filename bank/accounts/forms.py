from django.contrib.auth.forms import UserCreationForm 
from django import forms 
from .constants import ACCOUNT_TYPE , GENDER 
from django.contrib.auth.models import User
from .models import UserAddress ,UserBankAccounts

class UserRegistrationForm(UserCreationForm):
    
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type":'date'}))
    gender = forms.CharField(max_length=10,choices  = GENDER)
    street_address =  forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:

        model = User 
        fields = ["username","password1","password2","first_name","last_name","email"
                  "account_type","gender","postal_code","country"]
        
    def save(self,commit = True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()  # user model e data save korlam
            account_type = self.cleaned_data.get("accout_type")
            gender  = self.cleaned_data.get("gender")
            postal_code  = self.cleaned_data.get("postal_code")
            city = self.cleaned_data.get("city")
            country = self.cleaned_data.get("country")
            birth_date =self.cleaned_data.get("birth_date")
            street_address = self.cleaned_data('street_address')

            UserAddress.objects.create(
                user = our_user,
                city = city,
                postal_code = postal_code , 
                country = country,
                street_address = street_address,
                
            )
            UserBankAccounts.objects.create(
                user = our_user , 
                account_type = account_type , 
                birth_date = birth_date , 
                gender =  gender ,
                account_no = 100002 + our_user.id
            )

            return our_user 
        
          
            
            





    