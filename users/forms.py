from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm) :
    password1=forms.CharField(
        label='Password1',
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    password2=forms.CharField(
        label='Password2',
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

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)