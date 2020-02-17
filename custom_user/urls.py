from django.contrib import admin
from django.urls import path

import custom_user.views
from custom_user.models import MyCustomUser

urlpatterns = [
    path("home/", custom_user.views.home, name="home")
]