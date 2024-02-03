from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView
)
from django.shortcuts import (
    render,
    redirect,
)
from apps.tameenak_user.models import (
    TameenakCustomer,
    UserRequests
)
from apps.insurance_company.models import InsuranceCompany
from apps.tameenak_user.constants import (
    WAITING,
    PAID,
    REJECT
)
from apps.tameenak_user.models import UserRequests
from apps.tameenak_user.forms import UserRequestForm


def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Tameenak Admin').exists()


@method_decorator(user_passes_test(is_admin), name='dispatch')
class AdminDashboard(ListView):
    template_name = 'tameenak_user/tameenak_admin/admin_dashboard.html'

    def get_queryset(self):
        return UserRequests.objects.filter(
            request_status=WAITING
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_tameenak_user = TameenakCustomer.objects.count()
        total_insurance_company = InsuranceCompany.objects.count()
        total_waiting_requests = UserRequests.objects.filter(request_status=WAITING).count()
        context['form'] = UserRequestForm()
        context['object_list'] = self.get_queryset()
        context['total_tameenak_user'] = total_tameenak_user
        context['total_insurance_company'] = total_insurance_company
        context['total_waiting_requests'] = total_waiting_requests
        return context

    def post(self, request, *args, **kwargs):
        form = UserRequestForm(request.POST)
        if form.is_valid():
            action = request.POST.get('action')
            user_id = request.POST.get('user_id')
            rejection_reason = form.cleaned_data['rejection_reason']
            if action == 'accept_request':
                UserRequests.objects.filter(
                    user_id=user_id
                ).update(
                    request_status=PAID
                )
            elif action == 'reject_request':
                UserRequests.objects.filter(
                    user_id=user_id
                ).update(
                    request_status=REJECT,
                    rejection_reason=rejection_reason
                )
            return redirect('tameenak_admin:admin_dashboard')
        return render(
            request,
            self.template_name,
        )
