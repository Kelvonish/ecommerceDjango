from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
   attrs={
   'class':'form-control'
   }
    ) )
    username=forms.CharField(help_text='',max_length=100,widget=forms.TextInput(
   attrs={
   'class':'form-control'
   }
    ) )
    password1=forms.CharField(help_text='',max_length=100,label="Password",widget=forms.PasswordInput(
   attrs={
   'class':'form-control'
   }
    ) )
    password2=forms.CharField(help_text='', label="Confirm Password",max_length=100,widget=forms.PasswordInput(
   attrs={
   'class':'form-control'
   }
    ) )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
