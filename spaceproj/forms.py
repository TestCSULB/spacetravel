from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import ContactModel
# from . import settings

class AuthForm(AuthenticationForm):
    email = forms.EmailField(required=True)
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)


class createUserForm(UserCreationForm):
    class Meta:
        model=User
        #fields=['username','email','password1','password2']
        fields=['username','email','password1','password2']

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactModel
        # "UserName",
        fields=["FirstName","LastName","PhoneNumber","Address1","Address2","City","State","Zip","Country","DOB","InfoAboutUser","AdventuresInfo"]
        exclude=["owner"]