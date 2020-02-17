from django.db import models
from django.contrib.auth.models import AbstractUser

class MyCustomUser(AbstractUser):
    favorite_color = models.CharField(max_length=20)
    a = models.IntegerField(null=True, blank=True)