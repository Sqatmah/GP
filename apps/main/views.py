from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from apps.main.forms import LoginForm


class HomeView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
