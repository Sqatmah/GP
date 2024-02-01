from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.tameenak_user.models import (
    TameenakCustomer,
    InsuranceDegree,
    MedicalProfile
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
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
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


class DashboardSearchForm(forms.Form):
    order_by = forms.ChoiceField(
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
        queryset=InsuranceDegree.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ))
    name = forms.CharField(
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
        exclude = ('user', )

    def __init__(self):
        super().__init__()
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
