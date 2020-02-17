from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from custom_user.models import MyCustomUser

@login_required()
def home(request):
    items = MyCustomUser.objects.all()
    return render(request, "home.html", {"data": items})