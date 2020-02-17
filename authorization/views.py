from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from authorization.forms import SignupForm, LoginForm
from custom_user.models import MyCustomUser

def signup_view(request):
    html = "signup.html"

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyCustomUser.objects.create_user(
                data['name'],
                data['password']
            )
            login(request, user)
            MyCustomUser.objects.create(
                favorite_color=data['favorite_color'],
                a=data['a']
            )

            return HttpResponseRedirect("home")

    else:
        form = SignupForm()
    return render(request, html, {'form': form})

def login_view(request):
    html = "login.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            login(request, user)
            if user is not None:
                login(request, user)
                # Where we want to go next after logging in correctly
                return HttpResponseRedirect("/home/")
    else:
        form = LoginForm()
    return render(request, html, {'form': form})