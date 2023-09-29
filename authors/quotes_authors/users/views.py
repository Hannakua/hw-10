from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from django.contrib.messages import constants as messages


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to="authapp:main")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="authapp:main")
        else:
            return render(request, "users/signup.html", context={"form": form})

    return render(request, "users/signup.html", context={"form": RegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to="autheapp:main")

    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is None:
            messages.error(request, "Username or password didn't match")
            return redirect(to="users:login")

        login(request, user)
        return redirect(to="authapp:main")

    return render(request, "users/login.html", context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to="authapp:main")
