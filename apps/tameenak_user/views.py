from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.insurance_company import models
from apps.insurance_company import forms


def customerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'tameenak_user/../templates/tameenak_user/customerclick.html')


def customer_signup_view(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request, 'tameenak_user/../templates/tameenak_user/customersignup.html', context=mydict)


def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()


@login_required(login_url='customerlogin')
def customer_dashboard_view(request):
    dict = {
        'tameenak_user': models.Customer.objects.get(user_id=request.user.id),
        'available_policy': models.Policy.objects.all().count(),
        'applied_policy': models.PolicyRecord.objects.all().filter(
            customer=models.Customer.objects.get(user_id=request.user.id)).count(),
        'total_category': models.Category.objects.all().count(),
        'total_question': models.Question.objects.all().filter(
            customer=models.Customer.objects.get(user_id=request.user.id)).count(),

    }
    return render(request, 'tameenak_user/../templates/tameenak_user/customer_dashboard.html', context=dict)


def apply_policy_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    policies = models.Policy.objects.all()
    return render(request, 'tameenak_user/../templates/tameenak_user/apply_policy.html',
                  {'policies': policies, 'tameenak_user': customer})


def apply_view(request, pk):
    customer = models.Customer.objects.get(user_id=request.user.id)
    policy = models.Policy.objects.get(id=pk)
    policyrecord = models.PolicyRecord()
    policyrecord.Policy = policy
    policyrecord.customer = customer
    policyrecord.save()
    return redirect('history')


def history_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    policies = models.PolicyRecord.objects.all().filter(customer=customer)
    return render(request, 'tameenak_user/../templates/tameenak_user/history.html',
                  {'policies': policies, 'tameenak_user': customer})


def ask_question_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    questionForm = forms.QuestionForm()

    if request.method == 'POST':
        questionForm = forms.QuestionForm(request.POST)
        if questionForm.is_valid():
            question = questionForm.save(commit=False)
            question.customer = customer
            question.save()
            return redirect('question-history')
    return render(request, 'tameenak_user/../templates/tameenak_user/ask_question.html',
                  {'questionForm': questionForm, 'tameenak_user': customer})


def question_history_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    questions = models.Question.objects.all().filter(customer=customer)
    return render(request, 'tameenak_user/../templates/tameenak_user/question_history.html',
                  {'questions': questions, 'tameenak_user': customer})
