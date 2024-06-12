from django.shortcuts import render
from users.forms import RegisterForm
from users.forms import LoginForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username= form.cleaned_data()
            # name= form.cleaned_data()
            messages.success(request, f"{user.username}, your account has been created!")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})
