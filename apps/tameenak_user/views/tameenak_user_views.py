from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView,
    ListView
)
from django.shortcuts import (
    render,
    redirect
)
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.insurance_company.models import InsuranceCompany
from apps.tameenak_user.models import UserRequests
from apps.tameenak_user.constants import (
    PAID,
    WAITING
)
from apps.tameenak_user.forms import (
    BaseSignUpForm,
    DashboardSearchForm
)


class SignUp(FormView):
    form_class = BaseSignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    message = ''
    success = False

    def form_valid(self, form):
        user = form.save()
        user.groups.add(Group.objects.get(name='Tameenak Customer'))
        self.message = 'User created - please <a href="/login">login</a>.'
        self.success = True
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = self.message
        context['success'] = self.success
        return context

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        form = BaseSignUpForm()
        return render(request, self.template_name, {'form': form})


class UserDashboard(LoginRequiredMixin, ListView):
    template_name = 'user_dashboard.html'

    def get_queryset(self):
        return InsuranceCompany.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DashboardSearchForm()
        return context

    def post(self, request, *args, **kwargs):
        form = DashboardSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            order_by = form.cleaned_data['order_by']
            insurance_degree = form.cleaned_data['insurance_degree']

            q = Q()
            queryset = InsuranceCompany.objects.all()

            if name:
                q &= Q(name__icontains=name)
            if insurance_degree:
                q &= Q(insurance_degree__icontains=insurance_degree)
            queryset = queryset.filter(q)

            if order_by:
                queryset = queryset.order_by('name') if order_by == 'asc' else queryset.order_by('-name')
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                    'queryset': queryset
                }
            )
        return render(
            request,
            self.template_name,
            {
                'form': form
            }
        )


class RequestInsurance(LoginRequiredMixin, TemplateView):
    template_name = 'user_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insurance_company'] = InsuranceCompany.objects.get(id=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        insurance_company = InsuranceCompany.objects.get(id=self.kwargs['pk'])
        user_request = UserRequests.objects.get_or_create(
            user_id=request.user.id,
            insurance_company_id=insurance_company.id,
            insurance_degree_id=request.POST['insurance_degree'],
            request_status=WAITING
        )
        user_request.save()
        return redirect('dashboard')


class MedicalProfile(LoginRequiredMixin, FormView):
    form_class = MedicalProfileForm
    template_name = 'medical_profile.html'
    success_url = reverse_lazy('dashboard')
    message = ''

    def get(self, request, *args, **kwargs):
        form = MedicalProfileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = MedicalProfileForm(request.POST)
        if form.is_valid():
            form.save()
            self.message = 'Medical Profile created.'
            return HttpResponseRedirect(self.get_success_url())
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'message': self.message,
            }
        )


class HistoryView(LoginRequiredMixin, ListView):
    template_name = 'history.html'

    def get_queryset(self):
        return UserRequests.objects.select_related(
            'insurance_company'
        ).filter(
            user_id=self.request.user.id,
            request_status=PAID
        ).values_list(
            'insurance_company__logo',
            'insurance_company__name',
            'date_created',
            'insurance_company__address__city',
            'insurance_company__address__country',
            'insurance_company__address__street',
            'insurance_company__address__zip_code',
            'insurance_company__phone_number',
            'insurance_company__email',
            'insurance_company__website',
            'insurance_company__capital',
        )

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'object_list': self.get_queryset()})
