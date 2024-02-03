from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.main.models import Address
from apps.tameenak_user.models import (
    TameenakCustomer,
    InsuranceDegree,
    MedicalProfile,
    UserRequests
)


class BaseSignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        label='Password check',
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        widgets = {
            'password': forms.PasswordInput()
        }


class TameenakCustomerForm(forms.ModelForm):
    ex_subscription = forms.TypedChoiceField(
        choices=((True, 'Yes'), (False, 'No')),
        widget=forms.Select(attrs={'class': 'form-control'}),
        coerce=lambda x: x == 'True',
        label='Do you have an existing subscription?',
        initial=False,
    )

    class Meta:
        model = TameenakCustomer
        fields = '__all__'
        exclude = ('user', 'is_active', 'customer_status')

    def __init__(self, *args, **kwargs):
        super(TameenakCustomerForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Phone'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Address'})
        self.fields['role'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Role'})
        self.fields['picture'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Picture'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Gender'})


class DashboardSearchForm(forms.Form):
    order_by = forms.ChoiceField(
        required=False,
        choices=(
            ('asc', 'Ascending'),
            ('desc', 'Descending')
        ),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ))
    insurance_degree = forms.ModelChoiceField(
        required=False,
        queryset=InsuranceDegree.objects.all(),
    )
    name = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search",
                "class": "form-control"
            }
        ))

    def clean(self):
        return super().clean()


class MedicalProfileForm(forms.ModelForm):
    class Meta:
        model = MedicalProfile
        fields = '__all__'
        exclude = ('is_active', 'user')

    def __init__(self, *args, **kwargs):
        super(MedicalProfileForm, self).__init__(*args, **kwargs)
        self.fields['blood'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Blood'})
        self.fields['allergies'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Allergies'})
        self.fields['medical_conditions'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Medical Conditions'})
        self.fields['medical_history'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Medical History'})
        self.fields['current_medication'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Current Medication'})
        self.fields['family_medical_history'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Family Medical History'})
        self.fields['lifestyle_factors'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Lifestyle Factors'})
        self.fields['chronic_conditions'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Chronic Conditions'})
        self.fields['special_considerations'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Special Considerations'})


class UserRequestForm(forms.ModelForm):
    class Meta:
        model = UserRequests
        fields = ('rejection_reason', )

    def __init__(self, *args, **kwargs):
        super(UserRequestForm, self).__init__(*args, **kwargs)
        self.fields['rejection_reason'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Reject Response'})

        self.fields['rejection_reason'].required = False
