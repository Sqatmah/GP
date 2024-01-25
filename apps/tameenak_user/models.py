from django.db import models
from django.contrib.auth.models import User
from apps.insurance_company.models import InsuranceCompany
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
        return f"{self.user.user.first_name} - {self.role}"


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
        upload_to='image/tameenak_user/profile_pic/',
        default='image/tameenak_user/profile_pic/default_pic.png',
        null=False,
        blank=False,
    )
    ex_subscription = models.BooleanField(
        default=False
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

    def __str__(self):
        return f"{self.user.first_name}"


class InsuranceDegree(BaseModel):
    insurance_degree = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.insurance_degree}"


class UserRequests(BaseModel):
    user = models.ForeignKey(
        TameenakCustomer,
        on_delete=models.CASCADE
    )
    insurance_company = models.ForeignKey(
        InsuranceCompany,
        on_delete=models.CASCADE
    )
    insurance_degree = models.ForeignKey(
        InsuranceDegree,
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
