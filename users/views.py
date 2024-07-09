from django.forms import ValidationError
from django.shortcuts import render, HttpResponseRedirect
from users.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from users.forms import alpha

#Create your views here

#sign-up/register function being added to the databse
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        try:
                field_name='username'
                field_value = request.POST.get(field_name)
                alpha(field_value)
        
                if fm.is_valid():
            # uname = fm.cleaned_data['username']
            # alpha(uname)
            
                    messages.success(request, 'Account Created Successfully!')
                    fm.save()
        except ValidationError:
            messages.error(request, f"Username is not valid.")
    else:
        fm= SignUpForm()
    return render(request, 'users/signup.html',{'form':fm})

#login view function checking with the data base authenticating
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data= request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully')
                    return HttpResponseRedirect('/tasks/home/')
        else:
            fm = AuthenticationForm()
        return render(request,'users/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/tasks/home/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user/login/')