from . import forms
from django.shortcuts import render,redirect
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .constant import *
from django.contrib.auth.views import (
    LoginView
)
from django.views.generic import (
    TemplateView,
)
from django.contrib.auth import logout
from django.views.decorators.http import require_POST

class HomePage(TemplateView):
    template_name = "insurance/index.html" 

class LoginView(LoginView):
    template_name = 'insurance/adminlogin.html'


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request,'customer/customersignup.html',context=mydict)

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

@login_required
def user_logout(request):
    logout(request)
    return redirect('home_page') 

@login_required
def customer_dashboard_view(request):
    return render(request,'customer/customer_dashboard.html')


def search_form(request):
    query = request.GET.get('query', '')
    results = models.InsuranceCompany.objects.filter(name__icontains=query)  # Adjust based on your model fields

    if request.is_ajax():
        data = [{'id': result.id, 'name': result.name, 'description': result.description} for result in results]  # Adjust based on your model fields
        return JsonResponse({'results': data})

    context = {'query': query, 'results': results}
    return render(request, 'dashboard.html', context)


def medical_profile_form(request):
    if request.method == 'POST':
        form = forms.MedicalProfileForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a redirect or other actions after successful form submission
            return redirect('medical_profile_form_success')
    else:
        form = forms.MedicalProfileForm()

    return render(request, 'customer/medical_profile.html', {'form': form})


def medical_profile_form_success(request):
    return render(request, 'customer/medical_profile_success.html')


@require_POST
def submit_record_view(request):
    company_id = request.POST.get('record_id')
    user_id = request.user.id
    request = models.Requests.objects.create(
        user_id = user_id,
        insurance_company_id=company_id,
        request_status=WAIT
    )
    request.save()
    return JsonResponse({'success': True})
