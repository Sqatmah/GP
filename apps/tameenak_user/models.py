from django.db import models
from django.contrib.auth.models import User
from apps.insurance_company.models import (
    InsuranceCompany,
    InsuranceDegree
)
from apps.main.models import (
    BaseModel,
    Address
)
from apps.tameenak_user.constants import (
    USER_STATUS,
    GENDER,
    REQUEST_STATUS,
    ROLE_CHOICES
)


class Role(BaseModel):
    role = models.CharField(
        choices=ROLE_CHOICES,
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.role}"


class TameenakCustomer(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE
    )
    role = models.OneToOneField(
        Role,
        on_delete=models.CASCADE
    )
    picture = models.ImageField(
        upload_to='image/tameenak_user/tameenak_customer/profile_pic',
        default='image/tameenak_user/default_pic.png',
        null=False,
        blank=False,
    )
    ex_subscription = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    phone_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    customer_status = models.CharField(
        choices=USER_STATUS,
        max_length=50,
        null=True,
        blank=True,
    )
    gender = models.CharField(
        choices=GENDER,
        max_length=20,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.first_name}"


class UserRequests(BaseModel):
    user = models.ForeignKey(
        TameenakCustomer,
        on_delete=models.CASCADE
    )
    insurance_company = models.ForeignKey(
        InsuranceCompany,
        on_delete=models.CASCADE
    )
    request_status = models.CharField(
        choices=REQUEST_STATUS,
        max_length=100,
        blank=True,
        null=True,
    )
    rejection_reason = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    request_date = models.DateField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.user.first_name} - {self.request_status}"


class MedicalProfile(BaseModel):
    user = models.ForeignKey(
        TameenakCustomer,
        on_delete=models.CASCADE
    )
    blood = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    allergies = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    medical_conditions = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    medical_history = models.TextField(
        blank=True,
        null=True,
    )
    current_medication = models.TextField(
        blank=True,
        null=True,
    )
    family_medical_history = models.TextField(
        blank=True,
        null=True,
    )
    lifestyle_factors = models.TextField(
        blank=True,
        null=True,
    )
    chronic_conditions = models.TextField(
        blank=True,
        null=True,
    )
    special_considerations = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.user.first_name}"


class InsuranceEmployee(BaseModel):
    user = models.OneToOneField(
        TameenakCustomer,
        on_delete=models.CASCADE
    )
    insurance_company = models.ForeignKey(
        InsuranceCompany,
        on_delete=models.CASCADE
    )
    official_email = models.EmailField(
        max_length=100,
        null=True,
        blank=True,
    )
    job_title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    employee_status = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.user.first_name} employee at {self.insurance_company.name}"

