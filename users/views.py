from django.shortcuts import render, redirect
from users.forms import RegisterForm
from users.forms import LoginForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # username= form.cleaned_data()
            # name= form.cleaned_data()
            user = form.save()
            messages.success(
                request, f"{user.username}, your account has been created!"
            )
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('register')  # Redirect to the home page after successful login
#             else:
#                 messages.error(request, 'Invalid username or password')
#     else:
# #         form = LoginForm()
# #     return render(request, 'users/login.html', {'form': form})
# def login_view(request):
#     print("-------------------------------------")
#     print("request ",request)
#     print("request.method ",request.method)
#     if request.method == "POST":
#         print("request.POST ",request.POST)
#     # if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('register')
#             else:
#                 messages.error(request, 'Invalid username or password')
#     else:
#         form = LoginForm()
#     return render(request, 'users/login.html', {'form': form})


def login_view(request):
    print("-------------------------------------")
    print("request ", request)
    print("request.method ", request.method)
    if request.method == "POST":
        print("request.POST ", request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print("at line 68", f"Trying to authenticate: {username} / {password}")
            user = authenticate(request, username=username, password=password)
            print("at line 70", user)
            if user:
                print("at line 72", f"Authenticated user: {user}")
                if user.is_active:
                    login(request, user)
                    return redirect("register")
                else:
                    messages.error(request, "Account is inactive.")
            else:
                messages.error(request, "Invalid username or password")
                print("at line 84 Authentication failed")
        else:
            print("at line 86 Form is not valid")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})
