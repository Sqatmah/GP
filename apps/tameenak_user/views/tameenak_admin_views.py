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
from apps.tameenak_user.constants import WAITING
from apps.tameenak_user.models import UserRequests
from apps.tameenak_user.forms import (
    UserRequestForm,
    AddressForm
)


def is_admin(user):
    return user.is_authenticated and user.groups.filter(name='Tameenak Admin').exists()


@method_decorator(user_passes_test(is_admin), name='dispatch')
class AdminDashboard(TemplateView):
    template_name = 'tameenak_user/tameenak_admin/admin_dashboard.html'

    def get(self, request, *args, **kwargs):
        total_tameenak_user = TameenakCustomer.objects.count()
        total_insurance_company = InsuranceCompany.objects.count()
        total_waiting_requests = UserRequests.objects.filter(status=WAITING).count()

        return render(
            request,
            self.template_name, {
                'total_tameenak_user': total_tameenak_user,
                'total_insurance_company': total_insurance_company,
                'total_waiting_requests': total_waiting_requests,
            }
        )


@method_decorator(user_passes_test(is_admin), name='dispatch')
class AdminRequest(ListView):
    template_name = 'tameenak_user/tameenak_admin/admin_request.html'
    model = UserRequests
    paginate_by = 10

    def get_queryset(self):
        return UserRequests.objects.select_related(
            'insurance_company',
            'user'
        ).filter(
            status=WAITING
        ).order_by(
            '-created_at'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserRequestForm()
        return context

    def post(self, request, *args, **kwargs):
        form = UserRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tameenak_admin:user_request')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'object_list': self.get_queryset()
            }
        )


@method_decorator(user_passes_test(is_admin), name='dispatch')
class AdminAddress(FormView):
    form_class = AddressForm
    template_name = 'tameenak_user/tameenak_admin/admin_address.html'
    success_url = reverse_lazy('tameenak_admin:dashboard')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        form = AddressForm()
        address_query = Address.objects.all()
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'address_query': address_query
            }
        )








