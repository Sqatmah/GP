from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

from apps.tameenak_user.forms import BaseSignUpForm
from django.shortcuts import (
    render,
    redirect
)


# class HomeView(TemplateView):
#     template_name = 'home.html'


class Login(LoginView):
    template_name = 'login.html'


class SignUp(TemplateView):
    template_name = 'register.html'
    message = ''
    success = False

    def get(self, request, *args, **kwargs):
        form = BaseSignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = BaseSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            self.message = 'User created - please <a href="/login">login</a>.'
            self.success = True
            return redirect('login')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'message': self.message,
                'success': self.success
            }
        )



