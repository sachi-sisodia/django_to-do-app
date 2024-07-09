from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import  UserCreationForm
from django.core import validators

def alpha(value):
    if value[0].isnumeric():
        raise forms.ValidationError('Name should not start or contain numbers only')

class SignUpForm(UserCreationForm) :
    password1=forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    password2=forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'name','email'] 
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }
        labels = {'email':'Email'}
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)