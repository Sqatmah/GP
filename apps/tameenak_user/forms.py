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
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ))
    insurance_degree = forms.ModelChoiceField(
        queryset=InsuranceDegree.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ))
    name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search",
                "class": "form-control"
            }
        ))

    def clean(self):
        return super().clean()


class MedicalProfileForm(forms.ModelForm):
    blood = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Blood",
                "class": "form-control"
            }
        ))
    allergies = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Allergies",
                "class": "form-control"
            }
        ))
    medical_conditions = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Medical Conditions",
                "class": "form-control"
            }
        ))
    medical_history = forms.Textarea(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Medical History",
                "class": "form-control"
            }
        ))
    current_medication = forms.Textarea(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Current Medication",
                "class": "form-control"
            }
        ))
    family_medical_history = forms.Textarea(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Family Medical History",
                "class": "form-control"
            }
        ))
    lifestyle_factors = forms.Textarea(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Lifestyle Factors",
                "class": "form-control"
            }
        ))
    chronic_conditions = forms.Textarea(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Chronic Conditions",
                "class": "form-control"
            }
        ))
    special_considerations = forms.Textarea(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Special Considerations",
                "class": "form-control"
            }
        ))

    class Meta:
        model = MedicalProfile
        fields = '__all__'
        exclude = 'user'
