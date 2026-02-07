from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from vendor.models import Vendor


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,widget=forms.PasswordInput())
    

class VendorRegistrationForm(UserCreationForm):
    shop_name = forms.CharField(max_length=100)

    class Meta:
        model = User # Imp! user model is only saved while form.save() meta.model not meta.fields requires seperate saving
        fields = ['username','password1','password2','shop_name']