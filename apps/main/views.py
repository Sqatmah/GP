from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.shortcuts import redirect
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from apps.main.forms import LoginForm


class HomeView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    message = ''

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            self.message = 'Invalid credentials'
            return self.form_invalid(form)

        login(self.request, user)
        self.message = 'Login successful'
        if user.groups.filter(name='Tameenak Admin').exists():
            return redirect('tameenak_user:admin_dashboard')
        return redirect('tameenak_user:user_dashboard')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        context['msg'] = self.message
        return context


class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')
