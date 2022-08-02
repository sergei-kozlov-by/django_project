from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class LoginView(auth_views.LoginView):
    template_name = "user_app/login.html"
    next_page = "/"

class LogoutView(auth_views.LogoutView):
    template_name = "user_app/logout.html"

