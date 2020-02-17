from django.urls import path
import authorization.views

urlpatterns = [
    path("", authorization.views.signup_view, name="signup"),
    path("login/", authorization.views.login_view, name="login")
]