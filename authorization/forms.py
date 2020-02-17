from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25)
    favorite_color = forms.CharField(max_length=20)
    a = forms.IntegerField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25)