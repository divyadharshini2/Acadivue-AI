from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_page(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("/")

        return render(request, "accounts/login.html", {
            "error": "Invalid Email or Password"
        })

    return render(request, "accounts/login.html")


def register_page(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=email).exists():
            return render(request, "accounts/register.html", {
                "error": "Email already registered."
            })

        User.objects.create_user(
            username=email,
            email=email,
            first_name=full_name,
            password=password
        )

        return redirect("login")

    return render(request, "accounts/register.html")


def logout_page(request):
    logout(request)
    return redirect("login")