import logging
from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import (
    HttpResponseRedirect,
    HttpResponse
)
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView
)
from django.shortcuts import (
    render,
    redirect
)
from xhtml2pdf import pisa
from apps.insurance_company.models import InsuranceCompany
from apps.tameenak_user.models import (
    UserRequests,
    MedicalProfile
)
from apps.tameenak_user.constants import (
    PAID,
    WAITING
)
from apps.tameenak_user.forms import (
    BaseSignUpForm,
    TameenakCustomerForm,
    DashboardSearchForm,
    MedicalProfileForm
)


class SignUp(FormView):
    form_class = BaseSignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('main:custom_login')
    message = ''
    success = False

    def form_valid(self, form):
        user = form.save()
        tameenak_customer_form = TameenakCustomerForm(self.request.POST)
        if tameenak_customer_form.is_valid():
            tameenak_customer = tameenak_customer_form.save(commit=False)
            tameenak_customer.user = user
            tameenak_customer.save()
            self.message = 'User created - please <a href="/login">login</a>.'
            self.success = True
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BaseSignUpForm()
        context['tameenak_customer_form'] = TameenakCustomerForm()
        context['message'] = self.message
        context['success'] = self.success
        return context

    def form_invalid(self, form):
        logging.error('************************ Error in SignUp form_invalid method ************************')
        logging.error(form.errors)
        logging.error('************************ Error in SignUp form_invalid method ************************')
        return super().form_invalid(form)


class UserDashboard(LoginRequiredMixin, ListView):
    template_name = 'tameenak_user/customer/customer_dashboard.html'

    def get_queryset(self):
        return InsuranceCompany.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DashboardSearchForm()
        context['queryset'] = self.get_queryset()
        context['user_requests'] = UserRequests.objects.filter(
            user_id=self.request.user.tameenakcustomer.id,
        ).exists()
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
                q &= Q(insurance_degree__degree_type__icontains=insurance_degree)
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
                'form': form,
            }
        )


class RequestInsurance(LoginRequiredMixin, TemplateView):
    template_name = 'tameenak_user/customer/customer_dashboard.html'

    def post(self, request, *args, **kwargs):
        insurance_company = InsuranceCompany.objects.get(id=self.kwargs['pk'])
        try:
            user_request = UserRequests.objects.create(
                user_id=request.user.tameenakcustomer.id,
                insurance_company_id=insurance_company.id,
                request_status=WAITING
            )
            user_request.save()
        except Exception as e:
            logging.error('************************ Error in RequestInsurance post method ************************')
            logging.error(e)
            logging.error('************************ Error in RequestInsurance post method ************************')
        return redirect('tameenak_user:user_dashboard')


class MedicalProfileView(LoginRequiredMixin, FormView):
    form_class = MedicalProfileForm
    template_name = 'tameenak_user/customer/medical_profile.html'

    def get(self, request, *args, **kwargs):
        form = MedicalProfileForm()
        try:
            medical_query = MedicalProfile.objects.filter(user_id=request.user.tameenakcustomer.id).get()
        except MedicalProfile.DoesNotExist:
            medical_query = None
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'medical_query': medical_query
            }
        )

    def get_success_url(self):
        return reverse_lazy('tameenak_user:user_dashboard')

    def post(self, request, *args, **kwargs):
        form = MedicalProfileForm(request.POST)
        medical_profile, created = MedicalProfile.objects.get_or_create(user=request.user.tameenakcustomer)
        if form.is_valid():
            form = MedicalProfileForm(request.POST, instance=medical_profile)
            medical_profile = form.save(commit=False)
            medical_profile.user = request.user.tameenakcustomer
            medical_profile.save()
            return redirect(self.get_success_url())
        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )


class UserHistory(LoginRequiredMixin, ListView):
    template_name = 'tameenak_user/customer/user_history.html'

    def get_queryset(self):
        return UserRequests.objects.select_related(
            'insurance_company'
        ).filter(
            user_id=self.request.user.tameenakcustomer.id,
            request_status=PAID
        ).values(
            'insurance_company__name',
            'created_at',
            'insurance_company__address__city',
            'insurance_company__address__country',
            'insurance_company__address__street',
            'insurance_company__address__postal_code',
            'insurance_company__phone_number',
            'insurance_company__email',
            'insurance_company__website',
            'insurance_company__capital',
        )

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {
                'object_list': self.get_queryset()
            }
        )


class DownloadInsuranceDetails(LoginRequiredMixin, TemplateView):
    template_name = 'tameenak_user/customer/download_insurance_details.html'

    def get(self, request, *args, **kwargs):
        insurance_company = InsuranceCompany.objects.get(id=self.kwargs['pk'])

        context = {'insurance_company': insurance_company}
        template = get_template(self.template_name)
        html = template.render(context)

        # Create a PDF
        pdf_response = HttpResponse(content_type='application/pdf')
        pdf_response['Content-Disposition'] = f'attachment; filename="{insurance_company.name}_details.pdf"'

        # Generate PDF from HTML content
        pisa_status = pisa.CreatePDF(html, dest=pdf_response)
        if pisa_status.err:
            return HttpResponse('Error creating PDF', status=500)

        return pdf_response
