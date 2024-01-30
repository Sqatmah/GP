from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.shortcuts import (
    render,
    redirect
)


class AdminLogin(LoginView):
    template_name = 'login.html'


class AdminDashboard(TemplateView):
    template_name = 'tameenak_admin/admin_dashboard.html'


class AdminRequest(ListView):
    template_name = 'tameenak_admin/admin_request.html'
    model = Request
    context_object_name = 'requests'
    paginate_by = 10

    def get_queryset(self):
        return Request.objects.all().order_by('-created_at')




