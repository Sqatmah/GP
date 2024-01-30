from django.db import models
from apps.tameenak_user.models import TameenakCustomer
from apps.main.models import (
    BaseModel,
    Address
)


class InsuranceCompany(BaseModel):
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    logo = models.ImageField(
        upload_to='image/insurance_company/logo/',
        default='image/insurance_company/logo/default_logo.png'
    )
    email = models.EmailField(
        max_length=100,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    website = models.URLField(
        max_length=200,
        null=True,
        blank=True,
    )
    capital = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    established_date = models.DateField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} / {self.phone_number}"


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
