from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
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
            self.message = 'The User Is Not Exist!! Please Try To Register First'
            return self.form_invalid(form)
        if user.is_superuser:
            return render(self.request, 'layouts/page-401.html')

        self.message = 'Login successful'
        login(self.request, user)
        if user.groups.filter(name='Tameenak Admin').exists():
            return redirect('tameenak_admin:admin_dashboard')
        return redirect('tameenak_user:user_dashboard')

    def form_invalid(self, form):
        self.message = 'Invalid username or password. Please try again.'
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        context['msg'] = self.message
        return context


@login_required
def logout_view(request):
    logout(request)
    return redirect('main:home')

